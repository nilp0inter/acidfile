#!/usr/bin/env python
#-*- coding: utf-8 -*-

from glob import glob
from itertools import chain
import os
import tempfile

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

def before_scenario(context, scenario):
    context.example_filename = tempfile.mktemp()
    context.auxiliary_filename = tempfile.mktemp()
    context.random_data = os.urandom(1024)
    context.auxiliary_random_data = os.urandom(1024)


def after_scenario(context, scenario):
    for subfile in chain(glob(context.example_filename + '*'),
                         glob(context.auxiliary_filename + '*')):
        os.unlink(subfile)


def before_tag(context, tag):
    if tag == 'openfail':
        context.fail_schema = []

        def fail_open(*args, **kwargs):
            if args[0] in context.fail_schema:
                raise OSError
            else:
                return open(*args, **kwargs)

        m = Mock()
        m.side_effect = fail_open
        context.open_mocket = patch('acidfile.open',
                                    m, create=True)
        context.open_mocket.start()


def after_tag(context, tag):
    if tag == 'openfail':
        context.open_mocket.stop()

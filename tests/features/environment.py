#!/usr/bin/env python
#-*- coding: utf-8 -*-

from glob import glob
from itertools import chain
import os
import tempfile

def before_scenario(context, *args):
    context.example_filename = tempfile.mktemp()
    context.auxiliary_filename = tempfile.mktemp()
    context.random_data = os.urandom(1024)
    context.auxiliary_random_data = os.urandom(1024)

def after_scenario(context, *args):
    for subfile in chain(glob(context.example_filename + '*'),
                         glob(context.auxiliary_filename + '*')):
        os.unlink(subfile)

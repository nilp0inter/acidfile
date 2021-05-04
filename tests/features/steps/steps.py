# -*- coding: utf-8 -*-

import os
from glob import glob
import tempfile
from itertools import chain

from acidfile import ACIDFile

from behave import *


@given('an example acidfile')
def given_an_example_acidfile(context):
    context.example_acidfile = ACIDFile(context.example_filename, 'w')

@when('I write some data')
def when_i_write_some_data(context):
    context.example_acidfile.write(context.random_data)

@when('I write some auxiliary data')
def when_i_write_some_auxiliary_data(context):
    context.auxiliary_acidfile.write(context.auxiliary_random_data)

@when('I reopen it')
def and_i_reopen_it(context):
    context.example_acidfile.close()
    context.example_acidfile = ACIDFile(context.example_filename, 'r')

@then('I can read the same data')
def then_i_can_read_the_same_data(context):
    assert context.random_data == context.example_acidfile.read()

@when('I close the file')
def and_i_close_the_file(context):
    context.example_acidfile.close()

@when('I remove one of the inner files')
def and_i_remove_one_of_the_inner_files(context):
    prefix = context.example_filename
    innerfiles = glob(context.example_filename + '*')
    os.unlink(innerfiles[0])

@when('I open it again')
def and_i_open_it_again(context):
    context.example_acidfile = ACIDFile(context.example_filename, 'r')

@when('I remove all the inner files')
def and_i_remove_all_the_inner_files(context):
    prefix = context.example_filename
    innerfiles = glob(context.example_filename + '*')
    for innerfile in innerfiles:
        os.unlink(innerfile)

@then('I can\'t read any data')
def then_i_can_t_read_any_data(context):
    try:
        data = context.example_acidfile.read()
    except IOError:
        assert True
    else:
        assert False

@when('I corrupt one of the inner files')
def and_i_corrupt_one_of_the_inner_files(context):
    prefix = context.example_filename
    innerfiles = glob(context.example_filename + '*')
    with open(innerfiles[-1], 'wb') as f:
        f.write(os.urandom(1024))

@when('I corrupt all the inner files')
def and_i_corrupt_all_the_inner_files(context):
    prefix = context.example_filename
    innerfiles = glob(context.example_filename + '*')
    for innerfile in innerfiles:
        with open(innerfile, 'wb') as f:
            f.write(os.urandom(1024))

@given('an auxiliary acidfile')
def and_an_auxiliary_acidfile(context):
    context.auxiliary_acidfile = ACIDFile(context.auxiliary_filename, 'w')

@when('I close the auxiliary file')
def and_i_close_the_auxiliary_file(context):
    context.auxiliary_acidfile.close()

@when('replace example inner-file number {number} with auxiliary one')
def and_replace_example_inner_file_with_auxiliary_one(context, number):
    idx = int(number)
    try:
        os.unlink(context.example_filename + '.%s' % number)
    except FileNotFoundError:
        pass
    os.rename(context.auxiliary_filename + '.%s' % number,
              context.example_filename + '.%s' % number)

@when('seek to the start of the file')
def and_seek_to_the_start_of_the_file(context):
    context.example_acidfile.seek(0)

@then('I can open in a with statement and read the same data')
def then_i_can_open_in_a_with_statement_and_read_the_same_data(context):
    with ACIDFile(context.example_filename, 'r') as f:
        assert f.read() == context.random_data

@given('an acidfile written in a with statement')
def given_an_acidfile_written_in_a_with_statement(context):
    with ACIDFile(context.example_filename, 'w') as f:
        f.write(context.random_data)

@given('an example acidfile with no copies must raise on init')
def acidfile_with_no_copies_is_impossible(context):
    try:
        ACIDFile(context.example_filename, 'w', copies=0)
    except ValueError:
        assert True
    else:
        assert False

@given('an example acidfile with {number} copies')
def given_an_example_acidfile_with_number_copies(context, number):
    number = int(number)
    context.example_acidfile = ACIDFile(context.example_filename, 'w', copies=number)

@then('I can see {number} inner-files')
def then_i_can_see_number_inner_files(context, number):
    number = int(number)
    for i in range(number):
        assert os.path.exists(context.example_filename + '.%s' % i), "File idx %s does not exists." % i


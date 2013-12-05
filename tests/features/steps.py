# -*- coding: utf-8 -*-

import os
from glob import glob
import tempfile
from itertools import chain

from acidfile import ACIDFile

from lettuce import step, world, before, after

@before.all
def tempfiles():
    world.example_filename = tempfile.mktemp()
    world.auxiliary_filename = tempfile.mktemp()

@before.all
def randomdata():
    world.random_data = os.urandom(1024)
    world.auxiliary_random_data = os.urandom(1024)

@after.all
def delete_tempfiles(x):
    for subfile in chain(glob(world.example_filename + '*'),
                         glob(world.auxiliary_filename + '*')):
        os.unlink(subfile)

@step(u'^Given an example acidfile$')
def given_an_example_acidfile(step):
    world.example_acidfile = ACIDFile(world.example_filename, 'w')

@step(u'And I write some data')
@step(u'When I write some data')
def when_i_write_some_data(step):
    world.example_acidfile.write(world.random_data)

@step(u'When I write some auxiliary data')
def when_i_write_some_auxiliary_data(step):
    world.auxiliary_acidfile.write(world.auxiliary_random_data)

@step(u'And I reopen it')
def and_i_reopen_it(step):
    world.example_acidfile.close()
    world.example_acidfile = ACIDFile(world.example_filename, 'r')

@step(u'Then I can read the same data')
def then_i_can_read_the_same_data(step):
    assert world.random_data == world.example_acidfile.read()

@step(u'And I close the file')
def and_i_close_the_file(step):
    world.example_acidfile.close()

@step(u'And I remove one of the inner files')
def and_i_remove_one_of_the_inner_files(step):
    prefix = world.example_filename
    innerfiles = glob(world.example_filename + '*')
    os.unlink(innerfiles[0])

@step(u'And I open it again')
def and_i_open_it_again(step):
    world.example_acidfile = ACIDFile(world.example_filename, 'r')

@step(u'And I remove all the inner files')
def and_i_remove_all_the_inner_files(step):
    prefix = world.example_filename
    innerfiles = glob(world.example_filename + '*')
    for innerfile in innerfiles:
        os.unlink(innerfile)

@step(u'Then I can\'t read any data')
def then_i_can_t_read_any_data(step):
    try:
        data = world.example_acidfile.read()
    except IOError:
        assert True
    else:
        assert False

@step(u'And I corrupt one of the inner files')
def and_i_corrupt_one_of_the_inner_files(step):
    prefix = world.example_filename
    innerfiles = glob(world.example_filename + '*')
    with open(innerfiles[-1], 'w') as f:
        f.write(os.urandom(1024))

@step(u'And I corrupt all the inner files')
def and_i_corrupt_all_the_inner_files(step):
    prefix = world.example_filename
    innerfiles = glob(world.example_filename + '*')
    for innerfile in innerfiles:
        with open(innerfile, 'w') as f:
            f.write(os.urandom(1024))

@step(u'And an auxiliary acidfile')
def and_an_auxiliary_acidfile(step):
    world.auxiliary_acidfile = ACIDFile(world.auxiliary_filename, 'w')

@step(u'And I close the auxiliary file')
def and_i_close_the_auxiliary_file(step):
    world.auxiliary_acidfile.close()

@step(u'And replace example inner-file number (\d+) with auxiliary one')
def and_replace_example_inner_file_with_auxiliary_one(step, number):
    idx = int(number)
    os.rename(world.auxiliary_filename + '.%s' % number,
              world.example_filename + '.%s' % number)

@step(u'And seek to the start of the file')
def and_seek_to_the_start_of_the_file(step):
    world.example_acidfile.seek(0)

@step(u'Then I can open in a with statement and read the same data')
def then_i_can_open_in_a_with_statement_and_read_the_same_data(step):
    with ACIDFile(world.example_filename, 'r') as f:
        assert f.read() == world.random_data

@step(u'Given an acidfile written in a with statement')
def given_an_acidfile_written_in_a_with_statement(step):
    with ACIDFile(world.example_filename, 'w') as f:
        f.write(world.random_data)

@step(u'Given an example acidfile with no copies must raise on init')
def acidfile_with_no_copies_is_impossible(step):
    try:
        ACIDFile(world.example_filename, 'w', copies=0)
    except ValueError:
        assert True
    else:
        assert False

@step(u'Given an example acidfile with (\d+) copies')
def given_an_example_acidfile_with_number_copies(step, number):
    number = int(number)
    world.example_acidfile = ACIDFile(world.example_filename, 'w', copies=number)

@step(u'Then I can see (\d)+ inner-files')
def then_i_can_see_number_inner_files(step, number):
    number = int(number)
    for i in range(number):
        assert os.path.exists(world.example_filename + '.%s' % i), "File idx %s does not exists." % i

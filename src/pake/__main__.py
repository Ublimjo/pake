'''
Main entry point module
'''

import os
import imp
import click


def check_file(path='./', _file='_pake_.py'):
    '''
    check if _pake_.py file exist and valid
    '''
    working_directory = os.path.abspath(path)
    working_file = os.path.join(working_directory, _file)
    if os.path.isfile(working_file):
        return working_file
    return False


def execute(working_file, cmd):
    '''
    execute function in _pake_
    '''
    _pake_ = imp.load_source('_pake_', working_file)
    if cmd:
        for element in cmd:
            exec('_pake_.{}()'.format(element))
    else:
        for element in _pake_.NO_CMD:
            element()


@click.command()
@click.argument('cmd', nargs=-1)
def main(cmd):
    '''
    Tool which controls the generation of executables and other non-source
    files of a program from the program's source files
    '''
    working_file = check_file()
    if working_file:
        execute(working_file, cmd)
    else:
        print('_pake_.py file not found')

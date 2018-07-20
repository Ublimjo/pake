import os
import imp
import click


def check_file(path='./', _file='_pake_.py'):
    wd = os.path.abspath(path)
    wf = os.path.join(wd, _file)
    if os.path.isfile(wf):
        return wf
    else:
        return False


def execute(wf):
    _pake_ = imp.load_source('_pake_', wf)
    for element in _pake_.NO_CMD:
        element()


@click.command()
def main():
    wf = check_file()
    if wf:
        execute(wf)
    else:
        print('_pake_.py file not found')

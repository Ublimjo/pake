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


def execute(wf, cmd):
    _pake_ = imp.load_source('_pake_', wf)
    if cmd:
        for element in cmd:
            exec('_pake_.{}()'.format(element))
    else:
        for element in _pake_.NO_CMD:
            element()


@click.command()
@click.argument('cmd', nargs=-1)
def main(cmd):
    wf = check_file()
    if wf:
        execute(wf, cmd)
    else:
        print('_pake_.py file not found')

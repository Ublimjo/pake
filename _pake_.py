import os
import glob
from pake import command
from pake import x_


@command
def test():
    '''run test'''
    x_('python setup.py test')


@command
def clean():
    '''clean junk'''
    def recurse(path='*'):
        for name in glob.glob(path):
            if '__pycache__' in name:
                if os.path.isfile(name):
                    try:
                        os.remove(name)
                    except:
                        pass
                if os.path.isdir(name):
                    try:
                        os.removedirs(name)
                    except:
                        pass
            if os.path.isdir(name):
                recurse(name + '/*')

    recurse()
    recurse()


NO_CMD = [clean]

'''
All utility used by pake
'''

import os


def command(func):
    '''decorator for command'''
    def wraped(*arg, **kwargs):
        print(func.__doc__)
        return func()
    return wraped


def x_(arg):
    '''
    Small function to execute arg
    '''
    print('\t', arg)
    os.system(arg)

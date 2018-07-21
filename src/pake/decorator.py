'''
All decorator used by pake
'''

def command(func):
    def wraped(*arg, **kwargs):
        print(func.__doc__)
        return func()
    return wraped

from contextlib import contextmanager


class MyContextManager:

    def __enter__(self):
        print('pre enter into')
        return 'get ready'

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type == None:
            print('with no error')
        else:
            print('with an error (%s)' % exc_type)


with MyContextManager() as mt:
    print(mt)


@contextmanager
def decorator_context_mangager():
    print('glaekjgklaerjglae')
    yield 'good'
    print('gjkrlaglkaejlkgjlkaejklgr')


with decorator_context_mangager() as dcm:
    print(dcm)

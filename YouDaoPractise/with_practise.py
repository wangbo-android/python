import contextlib


@contextlib.contextmanager
def enter(name):
    print(name)
    yield
    print('jieshu')


e = enter('wangbo')
print(type(e))
with e as t:
    print('hao')

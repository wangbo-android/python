print('hello world')


def say(word):
    print(word)
    print(__name__)


def test():
    say('wangbo')


if __name__ == '__main__':
    test()

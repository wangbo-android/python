from Python3基础教程.chapter10 import hello
hello.say('wangbo')


class Foobar:

    name = ''

    def __init__(self, value):
        self.name = value


f = Foobar('this is value')
print(f.name)


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaaah....')
            self.hungry = False
        else:
            print('No,thanks!')


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()

class Person:
    name = ''

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print('Hello, world! I am {}'.format(self.name))


foo = Person()
bar = Person()

foo.set_name('foo')
bar.set_name('bar')
foo.greet()
bar.greet()


class Secretive:

    name = 'wangbo'

    def __sing(self):
        return self.name

    def song(self):
        print(self.name)
        print(self.__sing())


s = Secretive()
s.song()


class MemberCounter:

    member = 0

    def init(self):
        self.member += 1


m1 = MemberCounter()
print(m1.init())
print(m1.member)
m2 = MemberCounter()
print(m2.init())
print(m2.member)


class Filter:
    blocked = []

    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SubFilter(Filter):
    blocked = []

    def init(self):
        self.blocked = ['spam']


f = SubFilter()
f.init()
print(f.filter([1, 2, 3]))
print(issubclass(SubFilter, Filter))
print(SubFilter.__bases__)
print(isinstance(f, Filter))
print(isinstance(f, Filter))
print(f.__class__)
print(type(f))


class Calculator:

    value = ''

    def calculate(self, expression):
        self.value = eval(expression)


class Talker:

    value = ''

    def talk(self):
        print('Hi, my value is', self.value)


class TalkingCalculator(Calculator, Talker):
    pass


tc = TalkingCalculator()
tc.calculate('1 + 2 + 3')
tc.talk()
print(hasattr(tc, 'talk'))
print(hasattr(tc, 'front'))
print(hasattr(tc, 'calculate'))
print(callable(getattr(tc, 'talk', None)))
print(getattr(tc, 'talk', None))
setattr(tc, 'name', 'wangbo')
print(tc.name)
print(tc.__dict__)
print(getattr(tc, 'name'))

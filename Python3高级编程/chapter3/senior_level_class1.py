class Mama:

    def __init__(self, name, address):

        print(name + 'mama' + address)

    def says(self):
        print('I am mama')


class Child:
    def __init__(self, age, address):

        self.age = age
        self.address = address
        print(age + 'child' + address)

    def says(self):
        print('I am child')


class MyClass(Mama, Child):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age


m = MyClass('wangbo', '90')
m.says()
print('MRO:', [x.__name__ for x in MyClass.__mro__])






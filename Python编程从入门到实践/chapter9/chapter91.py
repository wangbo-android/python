param = (1, 3, 4)


def func1(x, y, z):

    print(x, y, z)


func1(*param)

param2 = {'name': 'wangbo', "age": 40}


def func2(name, age):

    print(name, age)


func2(**param2)


class Test:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(self.name)

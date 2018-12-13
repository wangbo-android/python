class RealAccess:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __get__(self, obj, owner):
        print('get func')
        return self.name, self.age

    def __set__(self, obj, value):
        self.name = value
        print('set func')

    @property
    def user_name(self):

        return self.name

    @user_name.setter
    def user_name(self, value):

        self.name = value


class MyClass(object):
    x = RealAccess('wangbo', 30)

    print(x.__dict__)

    def __init__(self):
        self.y = RealAccess('lisi', 30)


# m = MyClass()
# print(MyClass.__dict__)
# print(m.__dict__)
# print(m.x)
# print(m.y.name)
print(RealAccess('zhangsan', 30).user_name)





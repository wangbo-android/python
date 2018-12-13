class Practise:

    infos = []

    def get_infos(self):
        """次函数用来获取列表"""

        self.infos.append(3)
        return self.infos

    @staticmethod
    def greet_user(username='nothing'):

        print('Hello,' + username.title())

    @staticmethod
    def make_pizza(*toppings):

        for topping in toppings:
            print(topping)

    @staticmethod
    def build_profile(first, last, **user_info):

        profile = {}
        profile['first'] = first
        profile['last'] = last

        for key, value in user_info.items():

            profile[key] = value

        return profile

    @staticmethod
    def splite_profile(x, y):
        print(x, y)

    @staticmethod
    def splite_profile2(name, age):
        print(name + str(age))


Practise.greet_user(username='wangbo')
Practise.make_pizza('wangbo', 'zhangsan', 'lisi')
result = Practise.build_profile('wang', 'bo', location='shijiazhuang', field='physic')
print(result)
param = (3, 5)
param2 = {'name': 'wangbo', 'age': 30}
Practise.splite_profile(*param)
Practise.splite_profile2(**param2)
x, y, *z = [1, 2, 3, 4, 5, 6]
print(z)



def greet_user():
    print("hello world")


greet_user()


def show_info(*param):
    for p in param:
        print(p)


def show_info_show(**param):
    for key,value in param.items():
        print(key + value)


def show_num(name, age):
    print(name + age)


def show_num_show(x, y):
    print(x)
    print(y)


show_info(4, 3, 5, 'nihao')
show_info_show(name='wangbo', age='30', address='石家庄市')
show_num(**{'name': 'lihe', 'age': '30'})
show_num_show(*(3, 5))


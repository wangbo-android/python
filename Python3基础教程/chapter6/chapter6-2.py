def print_param(*params):
    print(params)


print_param('wnagbo', 'lisi')
x, y, *z = ['1', '2', '3', '4', '5']
print(z)


def print_param_2(title, **params):
    print(params)
    print(title)


print_param_2('helloworld', x=1, y=2, z=3)


labels = ['first', 'middle', 'last']
names = ['Luke Skywalker', 'Anakin Skywalker']
names.insert(1, '')
print(zip(labels, names))
print(list(zip(labels, names)))
for label, name in zip(labels, names):
    print(label, name)

def add(x, y):
    return x + y

params = (1, 2)
print(add(*params))


d = {'name': 'wangbo', 'age': '30'}


def infos(name, age):
    return name + age


print(infos(**d))
x = 1
scope = vars()
print(scope['x'])


def combin(parameter):
    print(parameter + globals()['paramter'])


paramter = 'berry'
combin(paramter)

print(list(map(lambda num: str(num), range(10))))
print([str(st) for st in range(10) if st > 1])
print(globals())
print(locals())
print(vars())
print(globals() == vars())

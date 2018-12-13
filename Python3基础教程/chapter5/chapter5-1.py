import math as footbar
print('I', 'wish', 'you', 'happy', sep=' ')
print('hello', end='!')
a = footbar.sqrt(4)
print(int(a))
values = 1, 2, 3
x, y, z = values
print(x)
scoundrel = {'name': 'wangbo', 'girlfriend': 'lihe'}
key, value = scoundrel.popitem()
print(key)
x, y, *rest = [1, 2, 3, 4, 5, 6]
print(rest)
print(bool('hello world'))
name = input('what is your name')
if name.endswith('wangbo'):
    print("wangbo")
elif name.endswith('lihe'):
    print('lihe')
else:
    print('none')
print(chr(128586))
name = input('what is you name') or 'unknown'
print(name)
name = input('what is you name') and 'unknown'
print(name)
# age = -1
# assert 0 < age < 100, 'The age must be realistic'
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)
for number in range(0, 101):
    print(number)
d = dict([('x', 1), ('y', 2), ('z', 3)])
print(d)
for key, value in d.items():
    print(key, value, sep='=')
x, y, *z = 'helloworld'
print(z)
names = ['wangbo', 'lihe', 'zhangsan', 'lisi']
ages = [30, 35, 59, 68]
for name, age in zip(names, ages):
    print(name, age, sep='=')


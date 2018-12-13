from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it")
print([x * x for x in range(10)])
print([x * x for x in range(10) if x % 3 == 0])
print([(x, y) for x in range(10) for y in range(20)])
squares = {i: '{} square is {}'.format(i, i**2) for i in range(10)}
print(squares)
name = 'Enid'
if name == 'Ralph Auldus Melish':
    print('Welcome')
elif name == 'Enid':
    pass
elif name == 'Bill Gates':
    print('Access Denied')
else:
    print('nothing')
scope = {}
exec('sqrt=1', scope)
sqrt(4)
print(scope)
print(eval('6 + 19 * 5'))






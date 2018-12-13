from copy import deepcopy
d = {};
d[42] = 'hello'
print(d)
l = [None] * 43
l[42] = '89'
print(l)
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
print(y)
x['username'] = 'wangbo'
y['machines'].remove('baz')
print(x)
print(y)
d = {}
d['name'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('Clive')
print(c)
print(dc)
d1 = {}.fromkeys(['name', 'age'])
print(d1)
d1['name'] = 'lisi'
d1['age'] = 30
print(d1)
d2 = dict.fromkeys(['address', 'number'], 'hello')
print(d2)
print(d2.get('name', '没有哟'))
d3 = dict([('name', 'wangbo'), ('age', '30')])
print(d3)
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())
it = d.items()
if ('spam', 0) in it:
    print(True)
else:
    print(False)
print(list(d.items()))
d4 = {'x': 1, 'y': 2}
print(d4.pop('x'))
print(d4)
d5 = {}
d5.setdefault('name', 'None')
print(d5)
print(d5['name'])
d6 = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'changed': '1111'}
d7 = {'title': 'Python Language Website', 'info': 'this is info'}
d6.update(d7)
print(d6)
print(list(d6.values()))
print(d6.keys())


import sys
import os

print(sys.argv)
print(os.sep)
print(os.pathsep)
print(os.linesep)
# os.system('E:' + os.sep + 'log.log')
print([1, 1, 2, 3])
print({'name': 'wangbo', 'name': 'lisi'})
print({1, 1, 2, 3, 4})
a = {1, 2, 3, 4}
b = {1, 3, 5, 6}
print(a.union(b))
print(a | b)
c = set()
d = frozenset()
print(c.add(d))

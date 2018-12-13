import copy

# for value in dir(copy):
#     print(value + '\r\n')
values = [n for n in dir(copy) if not n.startswith('_')]
for value in values:
    print(value + '\r\n')
help(copy.copy)
print(copy.__doc__)
print(range.__doc__)
print(copy.__file__)




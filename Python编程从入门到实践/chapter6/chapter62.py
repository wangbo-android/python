alien = dict()
alien['color'] = 'green'
alien['name'] = 'wangbo'
alien['age'] = '34'
print(alien.items())
for key, value in alien.items():
    print(key + value)
for key in alien.keys():
    print(key)
for value in alien.values():
    print(value)
alien['info'] = 'wangbo'
print(alien)
print(set(alien.values()))

from math import pi
# format = 'Hello, %s. %s enough for ya?'
# values = ('world', 'Hot')
# str = format % values
print(str)
print('{}, {}, and {}'.format('first', 'second', 'third'))
print('{0},{2},{1}'.format('1', '2', '3'))
print('{name} is appoximately {value:.2f}'.format(value=pi, name='pai'))
print(f"Euler's constant is roughly {pi:10.2f}")
print('{age},{1},{0},{address}'.format(1, 2, age=10, address='shijiazhuang'))
print('The number is {num:.3f}'.format(num=65))
print('The number is {shu:10}'.format(shu=10))
print('One googol is {:,}'.format(pow(10, 100)))




def compare(a, b):
	if a is b:
		print("a is b")
	elif a == b:
		print('a == b')
	elif type(a) is type(b):
		print('type a is type b')
	

l1 = list()
l2 = l1
compare(l1, l2)
print(dir(l1))
l3 = ['hello', 'world']
l4 = l3.copy()
l5 = l3[:]
del l4[1]
print(l3)
print(l4)
print(l5)

print(list({'name': 'wangbo', 'age': 30}.keys()))
print(list({'name': 'wangbo', 'age': 30}.values()))
print((type('hello world') is type(12)))
print(isinstance('helloworld', str))

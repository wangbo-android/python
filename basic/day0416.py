a = 'hello'
a += 'python'
print(a)
b = 'hello'
print(id(b))
c = b + 'world'
print(id(c))
print(id([1,2,3,4]))
print(hex(id([1,2,3,4])))
L = [1,2,3]
print(hex(id(L)))
L[0] = '1'
print(hex(id(L)))
print(2**2)
print('abc' < 'def')
print('ord')
a = 'hello'
print(type(a) == str)
print(isinstance(a,str))
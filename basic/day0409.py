import math
d = {
    'adam' : 98,
    'lisi' : 90,
    'zhangsan' : 87
}
print(len(d))
print(d['adam'])
print(d.get('lisi'))
if 'adam' in d:
    print(True)
print(d)
d['wangbo'] = 100
print(d)
for key in d:
    print(key)
    print(d[key])
s = set(['zhangli','wangwu','wangliu'])
print(s)
print(len(s))
print('zhangli' in s)
for name in s:
    print(name)
s1 = set([1,2,3,4])
s1.add(5)
print(s1)
s1.remove(5)
print(s1)
print(abs(-20))
print(int('123'))
print(str(123))
def countNum(x):
    print(x)
    return x
num = countNum(3)
print(num)

def move_math(x,y,step,range):
    nx = x + step * math.cos(range)
    ny = y + step * math.sin(range)
    return nx,ny
result = move_math(100,90,2,30)
print(result[0])
def getNum(*args):
    print(args)
getNum(1,2,3,4,5,6)
L = ['Adam','Tom','John','Tomcat']
print(L[1:3])
print(['3',])
ts = ('Adan',)
print(ts)
print('jgkrajgkjajgjkajkgjkla'[::2])
for index,name in enumerate(L):
    print(str(index) + '-' + str(name))
print('123' + '857' + '-')
for value in d.values():
    print(value)
print(d.values())
for key,value in d.items():
    print(str(key) + ':' + str(value))
print(d.items())
L = [x * x for x in range(1,11) if x % 2 == 0]
print(L)
for key,value in enumerate(L):
    print(str(key) + '-' + str(value))
print([m + n for m in 'ABC' for n in '123'])


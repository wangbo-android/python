print('hello',10)
age = 20
if age >=18:
    print('your age is',age)
    print('adult')
else:
    print("kids")
L = ['admin','lisi','wangb']
N = ('wangbo','zhangsan')
for name in L:
    print(name)
for name in N:
    print(name)
N = 10
x = 0
while x < N:
    print(x)
    x = x + 1
    if x == 5:
        break
print(x)
for x in ['A','B','C','D']:
    for y in ['1','2','3']:
        print(x + y)


for value in range(1, 5):
    print(value)
else:
    print("正常循环结束")
print(list(range(8)))
l = list(range(10))
print(max(l))
print(min(l))
print(sum(l))
squares = [value ** 2 for value in range(1, 100) if value % 2 == 0]
print(squares)
print(squares[-3:])

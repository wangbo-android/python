def square(x):
    'Calculates the square of number x.'
    return x * x


message = square.__doc__
print(message)
print(square(10))


def test():
    print('This is printed')
    return
    print('This is not')


test()
# print(x)


def say_hello(greeting='hello', word='world'):
    print(greeting + word)


say_hello()

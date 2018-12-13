from warnings import warn
from warnings import filterwarnings


class MyException(Exception):
    pass


try:
    x = int(input('Enter the first number:'))
    y = int(input('Enter the second number'))
    print(x / y)
except ZeroDivisionError:
    print('The second number can not be zero')
finally:
    print('This is finally block')


# try:
#     1/0
# except ZeroDivisionError:
#     raise ValueError from None

try:
    x = int(input('enter a first number'))
    y = int(input('enter a second number'))
    print(x / y)
except(ZeroDivisionError, TypeError, NameError, ValueError) as e:
    print('this is a exception occured')
    print(e)


while True:
    try:
        x = int(input('Enter the first number:'))
        y = int(input('Enter the second number:'))
        print(x / y)
    except Exception as e:
        print('Invalid input:', e)
        print('Please try again')
    else:
        break

filterwarnings('error')
filterwarnings('ignore', category=DeprecationWarning)
warn('I have a bad feeling', DeprecationWarning)

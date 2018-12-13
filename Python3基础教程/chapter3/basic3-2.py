from math import pi
str1 = 'This is what {0},{anything:10.3f},{1:,}'.format('hello', 2**100, anything=100)
print(str1)
str2 = 'this is {:,}'.format(2**100)
print(str2)
str3 = f'this is what {pi:10.6f}'
print(str3)
str4 = 'this is name {:.5}'.format('hwllojkjkr')
print(str4)
str5 = f'this is waht {pi:010.6f}'
print(str5)
str6 = '{0:<10.3f}\n{0:>10.3f}\n{0:^10.3f}'.format(pi)
print(str6)
str7 = f'this is waht {pi:&^20.6f}'
print(str7)
str8 = 'this is hatath {0:>-#010.2f}'.format(-pi)
print(str8)
str9 = 'this is shaut {0:#10b}'.format(10)
print(str9)
tu = tuple('shit')
print(tu)
print(list('fucking'))
print('The middle by Jimy Eat World'.center(39, '*'))
print('The middle by'.find('b', 0, 11))
numStr = '1+2+3+4+5+6'
print(numStr.split('+'))
print(type(numStr.split('+')))
table = str.maketrans('cs', 'kz')
print(table)
print('    this is an incredible test  $  !'.translate(table).strip(' $!').isdigit())


















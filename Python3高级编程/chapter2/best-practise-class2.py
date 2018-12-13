def pythongd():
    print('please input word')
    while True:
        answer = (yield)
        if answer == 'yes':
            continue
        else:
           break
    else:
        print('end')


p = pythongd()
next(p)
p.send('yes')

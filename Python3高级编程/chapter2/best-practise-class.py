class Basic:

    @staticmethod
    def best_practise():
        print(list(b'hello'))
        print(tuple(b'world'))
        b = 'fuck'.encode('utf-8', 'something wrong')
        print(list(b))
        print(type(b))
        print(b.decode('utf-8'))
        print([i for i in range(10) if i % 2 == 0])
        for i, v in enumerate(list(range(20))):
            print(str(i) + ':' + str(v))
        for item in zip(['2', '5', '7'], ['3', '4', '9']):
            print(type(item))
        t1 = (1, 4)
        t2 = (2, 5)
        t3 = (3, 6)
        print(list(zip(t1, t2, t3)))
        first, second, third = 'helo', 'kworld', 'fuck'
        print(second)
        i = iter([n for n in range(100)])
        # print(next(i))
        # while True:
        #     try:
        #         print(next(i))
        #     except StopIteration as e:
        #         print('exception occurd')
        #         raise e
        # else:
        #     print('everything is fine')


Basic.best_practise()


class Basic2:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self


for element in Basic2(4):
    print(element)

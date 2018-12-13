class MyClass:

    @staticmethod
    def smeth():
        print('this is a static method')

    @classmethod
    def cmeth(cls):
        print('this is a class method', cls)


MyClass.smeth()
MyClass.cmeth()
print()


class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


t = TestIterator()
print(list(t))


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


nested = [[1, 2], [3, 4], [5]]
print(list(flatten(nested)))
i = iter([1, 2, 3, 4])
print(next(i))


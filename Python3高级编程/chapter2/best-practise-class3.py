def drug_price(func):

    def wrapper(self, *args, **kwargs):
        print(self, args, kwargs)
        self.price += 2
        return func(self, *args, **kwargs)

    return wrapper


class Food:

    def __init__(self, price):
        self.price = price

    @drug_price
    def get_price(self):
        return self.price


if __name__ == '__main__':

    f = Food(100)
    result = f.get_price()
    print(result)



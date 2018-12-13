from chapter9 import Test


class Car:
    def __init__(self, model, create_time):
        self.model = model
        self.createTime = create_time

    def show_info(self):
        print(self.createTime, self.model)


class Battary:
    def __init__(self, price, year):
        self.price = price
        self.year = year

    def print_info(self):
        print(self.year + self.price)


class Moto(Car):
    def __init__(self, model, create_time):
        super().__init__(model, create_time)
        self.model = model
        self.createTime = create_time
        self.battary = Battary('100', '2018-07-25')
        self.battary.print_info()

    def show_info(self):
        print('this is sub class info print')


moto = Moto('electric', '2018-07-25')
moto.show_info()
test = Test('wangbo')

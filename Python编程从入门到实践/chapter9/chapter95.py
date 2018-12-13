class Car:
    def __init__(self, name, info, price):
        self.name = name
        self.info = info
        self.price = price

    def get_description(self):
        print(self.name + self.info + str(self.price))

    def read_info(self, name):
        self.name = name
        print(self.name)


class ElectricMoto(Car):
    def __init__(self, name, info, price):
        super().__init__(name, info, price)


electricMoto = ElectricMoto('wangbo', 'motototo', 60000)
electricMoto.get_description()
electricMoto.read_info('lisan')


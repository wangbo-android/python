class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def show_car(self):
        print(self.odometer_reading)

    def show_infos(self):
        print(self.make + self.model + self.year)


class ElectricMoto(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


dog = Dog('muyang', 10)
dog.sit()
dog.roll_over()
car = Car('shijiazhuang', 'model', '2018-07-23')
car.show_car()
elec = ElectricMoto('tianjin', 'mode s', '2018-07-24')
elec.show_infos()

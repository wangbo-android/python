class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.recording = 0

    def sit(self):
        print(self.name)

    def roll_over(self):
        print(self.age)


dog = Dog('123', 10)
dog.sit()
dog2 = Dog('456', 11)
dog2.sit()
dog.recording = 10
print(dog.recording)


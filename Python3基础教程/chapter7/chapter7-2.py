from abc import ABC, abstractmethod


class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass


class Knigget(Talker):
    def talk(self):
        print('Hi')


k = Knigget()
k.talk()
print(isinstance(k, Talker))


class Herring:
    def talk(self):
        print('Blub')


Talker.register(Herring)
h = Herring()
print(isinstance(h, Talker))

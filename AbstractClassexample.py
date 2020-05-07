from abc import abstractclassmethod, ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("In new class")
        print("Hey")


# com = Computer()
# com.process()
l1 = Laptop()
l1.process()

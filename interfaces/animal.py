from abc import ABC, abstractmethod

class InterfaceAnimal(ABC):
    @abstractmethod
    def breathe(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass
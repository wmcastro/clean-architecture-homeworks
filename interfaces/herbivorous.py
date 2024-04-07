from abc import abstractmethod

from interfaces.animal import InterfaceAnimal

class InterfaceHerbivorous(InterfaceAnimal):
    @abstractmethod
    def eat_vegetables(self):
        pass
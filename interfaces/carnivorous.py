from abc import abstractmethod

from interfaces.animal import InterfaceAnimal

class InterfaceCarnivorous(InterfaceAnimal):
    @abstractmethod
    def eat_meet(self):
        pass
    
    @abstractmethod
    def fang_size(self):
        pass
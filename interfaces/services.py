from abc import ABC, abstractmethod

class InterfaceService(ABC):
    @abstractmethod
    def get_entity(self):
        pass
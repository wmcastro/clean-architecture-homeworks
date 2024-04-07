from abc import ABC, abstractmethod

class InterfaceDAO(ABC):
    @abstractmethod
    def get_session(self, entity):
        pass

    @abstractmethod
    def close_connection(self):
        pass
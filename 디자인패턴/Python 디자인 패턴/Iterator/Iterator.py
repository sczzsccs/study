from abc import *
class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def next()->bool:pass
    
    @abstractmethod
    def current()->None:pass
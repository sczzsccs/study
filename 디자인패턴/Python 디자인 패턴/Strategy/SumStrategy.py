from abc import*
class SumStrategy(metaclass=ABCMeta):
    @abstractmethod
    def get(this, N:int)->int:
        pass
    pass
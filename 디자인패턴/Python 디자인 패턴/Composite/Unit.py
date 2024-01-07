from abc import*
class Unit(metaclass=ABCMeta):
    def __init__(this, name) -> None:
        this.name = name
    
    @abstractmethod
    def getSize():pass
    pass
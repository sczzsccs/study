from abc import*
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(this, name) -> None:
        this.name = name
    
    @abstractmethod
    def sound(this):pass
    pass
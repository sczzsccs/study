from abc import*
class Display(metaclass=ABCMeta):
    @abstractmethod
    def title(this, draft):pass
    @abstractmethod
    def author(this, draft):pass
    @abstractmethod
    def content(this, draft):pass
    pass
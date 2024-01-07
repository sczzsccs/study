from abc import*
from Item import*
class Factory(ABC):
    @abstractmethod
    def isCreatable(this, name:str)->bool:pass
    @abstractmethod
    def CreateItem(this, name:str)->Item:pass
    @abstractmethod
    def postProcessItem(this, name:str):pass
    
    def create(this, name:str)->Item:
        if(this.isCreatable(name=name)):
            this.postProcessItem(name=name)
            return this.CreateItem(name=name)
        else:pass
    pass
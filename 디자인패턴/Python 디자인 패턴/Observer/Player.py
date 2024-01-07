from abc import*
class Player(ABC):
    def __init__(this, name: str) -> None:
        this.name = name
    
    def getPlayerName(this):
        return this.name
    
    @abstractmethod
    def Update(this, diceNum: int) -> None:pass
    pass
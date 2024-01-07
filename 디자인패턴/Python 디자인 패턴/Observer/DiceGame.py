from abc import*
from Player import*
class DiceGame(ABC):
    Players:list = []
    def addPlay(this, player:Player):
        this.Players.append(player)
    
    @abstractmethod
    def Play(this):pass
    pass
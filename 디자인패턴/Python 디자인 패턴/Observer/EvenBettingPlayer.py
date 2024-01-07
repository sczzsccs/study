from Player import*
class EvenBettingPlayer(Player):
    def __init__(this, name: str) -> None:
        super().__init__(name)
    
    def Update(this, diceNum: int) -> None:
        print(f"\nPlayer: {this.getPlayerName()}")
        if(diceNum%2==0):print("Win")
        else:print("Lose!")
        pass
    pass
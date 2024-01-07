from Player import*
class OddBettingPlayer(Player):
    def __init__(this, name: str) -> None:
        super().__init__(name)
    
    def Update(this, diceNum: int) -> None:
        print(f"\nPlayer: {this.getPlayerName()}")
        if(diceNum%2):print("Win")
        else:print("Lose!")
        pass
    pass
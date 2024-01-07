from Player import*
class nBettingPlayer(Player):
    def __init__(this, name: str, num: int) -> None:
        super().__init__(name)
        this.num = num
    
    def Update(this, diceNum: int) -> None:
        print(f"\nPlayer: {this.getPlayerName()}")
        print(f"Plck Number: {this.num}")
        if(diceNum==this.num):print("Win")
        else:print("Lose!")
        pass
    pass
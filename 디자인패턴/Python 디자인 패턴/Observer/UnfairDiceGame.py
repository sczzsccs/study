from DiceGame import*
import random as rd
class UnfairDiceGame(DiceGame):
    def Play(this):
        diceNum = rd.randrange(20)+1
        if(diceNum > 6): diceNum = 2
        print(f"Current: {diceNum}")
        players = iter(this.Players)
        player = next(players)
        while(player):
            player.Update(diceNum)
            player = next(players, 0)
        pass
    pass
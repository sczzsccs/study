from DiceGame import*
import random as rd
class FairDiceGame(DiceGame):
    def Play(this):
        diceNum = rd.randrange(6)+1
        print(f"Current: {diceNum}")
        players = iter(this.Players)
        player = next(players)
        while(player):
            player.Update(diceNum)
            player = next(players, 0)
        pass
    pass
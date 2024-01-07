from FairDiceGame import*
from UnfairDiceGame import*

from OddBettingPlayer import*
from EvenBettingPlayer import*
from nBettingPlayer import*

Players = UnfairDiceGame()
Players.addPlay(OddBettingPlayer("짝궁댕이"))
Players.addPlay(nBettingPlayer("홀쭉이", 2))
Players.addPlay(EvenBettingPlayer("홀아비"))

Players.Play()
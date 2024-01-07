from abc import*
from Mediator import*

class Participant(ABC):
    def __init__(self, mediator:Mediator) -> None:
        self.mediator = mediator
    pass
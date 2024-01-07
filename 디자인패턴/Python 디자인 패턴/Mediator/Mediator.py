from abc import*

class Mediator(ABC):
    @abstractmethod
    def participantChange(this, participant):pass
    pass
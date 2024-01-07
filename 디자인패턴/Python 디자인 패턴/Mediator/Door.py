from Participant import*

class Door(Participant):
    def __init__(this, mediator: Mediator) -> None:
        super().__init__(mediator)
        this.bDoor = False
    
    def Open(this):
        this.bDoor = True
        this.mediator.participantChange(this)
    
    def Close(this):
        this.bDoor = False
        this.mediator.participantChange(this)
    
    def isDoor(this):
        return this.bDoor
    
    def strPrint(this):
        if(this.bDoor):return "# 문 열림"
        return "# 문 닫힘"
    pass
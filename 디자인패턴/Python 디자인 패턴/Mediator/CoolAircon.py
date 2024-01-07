from Participant import*

class CoolAircon(Participant):
    def __init__(this, mediator: Mediator) -> None:
        super().__init__(mediator)
        this.bAircon = False
    
    def On(this):
        this.bAircon = True
        this.mediator.participantChange(this)
    
    def Off(this):
        this.bAircon = False
        this.mediator.participantChange(this)
    
    def isAircon(this):
        return this.bAircon
    
    def strPrint(this):
        if(this.bAircon):return "# 에어컨 켜짐"
        return "# 에어컨 꺼짐"
    pass
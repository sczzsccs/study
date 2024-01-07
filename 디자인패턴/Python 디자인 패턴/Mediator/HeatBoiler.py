from Participant import*

class HeatBoiler(Participant):
    def __init__(this, mediator: Mediator) -> None:
        super().__init__(mediator)
        this.bBoiler = False
    
    def On(this):
        this.bBoiler = True
        this.mediator.participantChange(this)
    
    def Off(this):
        this.bBoiler = False
        this.mediator.participantChange(this)
    
    def isBoiler(this):
        return this.bBoiler
    
    def strPrint(this):
        if(this.bBoiler):return "# 보일러 켜짐"
        return "# 보일러 꺼짐"
    pass
from Participant import*

class Window(Participant):
    def __init__(this, mediator: Mediator) -> None:
        super().__init__(mediator)
        this.bWindow = False
    
    def Open(this):
        this.bWindow = True
        this.mediator.participantChange(this)
    
    def Close(this):
        this.bWindow = False
        this.mediator.participantChange(this)
    
    def isWindow(this):
        return this.bWindow
    
    def strPrint(this):
        if(this.bWindow):return "# 창문 열림"
        return "# 창문 닫힘"
    pass
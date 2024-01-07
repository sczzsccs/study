from Mediator import*

from Door import*
from Window import*
from CoolAircon import*
from HeatBoiler import*

class SmartHome (Mediator):
    def __init__(this) -> None:
        this.PartiMedi = {
            "door":Door(this),
            "window":Window(this),
            "aircon":CoolAircon(this),
            "boiler":HeatBoiler(this)
        }
    
    def participantChange(this, participant:Participant)->None:
        if((participant==this.PartiMedi["door"] and
            this.PartiMedi["door"].isDoor())
            or (participant==this.PartiMedi["window"] and
            this.PartiMedi["window"].isWindow())):
            this.PartiMedi["aircon"].Off()
            this.PartiMedi["boiler"].Off()
        elif(participant==this.PartiMedi["aircon"] and
            this.PartiMedi["aircon"].isAircon()):
            this.PartiMedi["door"].Close()
            this.PartiMedi["window"].Close()
            this.PartiMedi["boiler"].Off()
        elif(participant==this.PartiMedi["boiler"] and
            this.PartiMedi["boiler"].isBoiler()):
            this.PartiMedi["door"].Close()
            this.PartiMedi["window"].Close()
            this.PartiMedi["aircon"].Off()
    
    def report(this):
        print("[집안 상태]")
        print(this.PartiMedi["door"].strPrint())
        print(this.PartiMedi["window"].strPrint())
        print(this.PartiMedi["aircon"].strPrint())
        print(this.PartiMedi["boiler"].strPrint())
        print()
    pass
from Animal import*
from Tiger import Tiger as Tig
class Tiger(Animal):
    def __init__(this, name) -> None:
        this.tiger = Tig()
        this.tiger.SetName(name=name)
        super().__init__(this.tiger.GetName())
    
    def sound(this):
        return this.name + " " + this.tiger.roar()
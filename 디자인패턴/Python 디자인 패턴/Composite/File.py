from Unit import*
class File(Unit):
    def __init__(this, name, size) -> None:
        super().__init__(name)
        this.size = size
    
    def getSize(this):
        return this.size
    pass
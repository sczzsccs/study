from File import*
class Folder(Unit):
    def __init__(this, name) -> None:
        super().__init__(name)
        this.unitList = []
    
    def getSize(this)->int:
        this.size = 0
        it  = iter(this.unitList)
        
        unit_it = next(it, 0)
        while(unit_it):
            this.size += unit_it.getSize()
            unit_it = next(it, 0)
        return this.size
    
    def add(this, unit:Unit)->bool:
        this.unitList.append(unit)
        return True
    
    def Listed(this, indent:str, unit:Unit):
        if(type(unit)==File):
            print(f"{indent} {unit.name}({unit.getSize()})")
        else:
            it  = iter(unit.unitList)
            print(f"{indent}+ {unit.name}({unit.getSize()})")
            unit_it = next(it, 0)
            while(unit_it):
                this.Listed(indent=f"{indent}\t", unit=unit_it)
                unit_it = next(it, 0)
        pass
    
    def List(this):
        this.Listed(indent="", unit=this)
    pass
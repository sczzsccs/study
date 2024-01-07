from Animal import*
class Dog(Animal):
    def __init__(this, name) -> None:
        super().__init__(name)
    
    def sound(this)->str:
        return this.name + " Brakinkg"
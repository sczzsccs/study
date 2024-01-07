class My_Item():
    def __init__(self, name:str, cost:int) -> None:
        self.name = name
        self.cost = cost
        pass

    def toString(self)->str:
        return f"({self.name}, {self.cost})"
    pass
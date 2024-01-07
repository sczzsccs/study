from Factory import*
from Item import Item
from ItemCreate import*

class ItemData():
        def __init__(this, maxCount:int) -> None:
            this.MaxCount = maxCount
            this.CurrentCount = 0
        pass

class ItemFactory(Factory):
    def __init__(this) -> None:
        this.Repository = {}
        this.Repository["sword"] = ItemData(maxCount=3)
        this.Repository["shield"] = ItemData(maxCount=2)
        this.Repository["bow"] = ItemData(maxCount=1)
    
    def isCreatable(this, name: str) -> bool:        
        if(this.Repository[name]==None):
            print(f"잘못된 아이템이름 {name}")
            itemCheck = False
        elif(this.Repository[name].CurrentCount 
                >= this.Repository[name].MaxCount):
            
            # TypeError: '>='은 'int'와 'ItemData' 
            # 인스턴스 간에는 지원되지 않습니다.
            print(f"재고없는 아이템이름 {name}")
            itemCheck = False
        else:itemCheck = True
        return itemCheck
    
    def CreateItem(this, name: str) -> Item:
        if(name=="sword"):item=Sword()
        elif(name=="shield"):item=Shield()
        elif(name=="bow"):item=Bow()
        else: 
            print(f"잘못된 아이템이름 {name}")
            return None
        return item
    
    def postProcessItem(this, name: str)->None:
        this.Repository[name].CurrentCount+=1
        pass
    pass
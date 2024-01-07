from ArrayIterator import*
from My_Item import My_Item as itm

items = [
    itm(name="CPU", cost=1000),
    itm(name="KeyBoard", cost=2000),
    itm(name="Mouse", cost=3000),
    itm(name="HDD", cost=50)
]

it = ArrayIterator(Array(items))

while(it.next()):
    ones = it.current()
    print(ones.toString())
    pass
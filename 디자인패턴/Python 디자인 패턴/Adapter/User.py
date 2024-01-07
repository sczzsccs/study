from Dog import*
from Cat import*
from TigerAdapter import*

animals = []
animals.append(Dog("댕이"))
animals.append(Cat("솜털이"))
animals.append(Dog("츄츄"))
animals.append(Tiger("타이온"))

for animal in animals:
    print(animal.sound())
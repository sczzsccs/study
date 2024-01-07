from ItemFactory import*

itemfactory = ItemFactory()

item = itemfactory.create(name="sword")
item.use()
item = itemfactory.create(name="sword")
item.use()
item = itemfactory.create(name="sword")
item.use()
itemfactory.create(name="sword")
itemfactory.create(name="sword")

item = itemfactory.create(name="shield")
item.use()
item = itemfactory.create(name="shield")
itemfactory.create(name="shield")
item.use()
item.use()

item = itemfactory.create(name="bow")
item.use()
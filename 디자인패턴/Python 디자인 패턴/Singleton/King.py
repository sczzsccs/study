class King:
    @classmethod
    def getInstance(this):
        return this
    
    def say():
        print("I am only one..")
    pass

king = King.getInstance()
king.say()

king2 = King.getInstance()

if(king == king2):
    print("seam object")
else:
    print("different object")
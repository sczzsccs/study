from Digit import*
class DigitFactory():
    pool = ["", "", "", "", "",
            "", "", "", "", ""]
    def getDigit(this, n:int)->Digit:
        if(this.pool[n] != ""):
            return this.pool[n]
        else:
            digit = Digit(f'./deta/{n}.txt')
            return digit.getData()
    pass
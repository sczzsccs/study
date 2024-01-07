from DigitFactory import*
class Number():
    digits = []
    def __init__(this, number:int) -> None:
        strNum = str(number)
        Dgifac = DigitFactory()
        strNum_len = len(strNum)
        for i in range(strNum_len):
            this.digits.append(Dgifac.getDigit(int(strNum[i])))
    
    def NumPrint(this):
        Digits_len = len(this.digits)
        for i in range(Digits_len):
            print(this.digits[i]+"\n")
    pass
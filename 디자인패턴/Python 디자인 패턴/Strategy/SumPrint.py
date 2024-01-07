from SumStrategy import*
class SumPrint():
    def Print(this, sumstrategy:SumStrategy, N:int):
        print(f"The Sum of 1 - {N} :", end=" ")
        print(f"{sumstrategy.get(N)}")
    pass
from SumStrategy import*
class GaussSumStrategy(SumStrategy):
    def get(this, N:int)->int:
        return int((1+N)*N/2)
    pass
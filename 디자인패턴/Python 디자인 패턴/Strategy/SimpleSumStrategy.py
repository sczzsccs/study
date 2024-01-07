from SumStrategy import*
class SimpleStrategy(SumStrategy):
    def get(this, N):
        sum = 0
        for i in range(N+1):
            sum += i
        return sum
    pass
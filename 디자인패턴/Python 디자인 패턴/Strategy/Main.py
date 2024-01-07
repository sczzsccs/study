from SumPrint import*
from SimpleSumStrategy import*
from GaussSumStrategy import*

cal = SumPrint()
cal.Print(sumstrategy=SimpleStrategy(), N=10)
cal.Print(sumstrategy=GaussSumStrategy(), N=10)

import 'SumStrategy.dart';

class SumPrinter {
  void Print(SumStrategy sumstrategy, int N) {
    print("The Sum of 1 - $N : ${sumstrategy.get(N)}");
  }
}
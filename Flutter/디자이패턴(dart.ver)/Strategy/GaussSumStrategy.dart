import 'SumStrategy.dart';

class GaussSumStartegy implements SumStrategy {
  @override
  int get(int N) { 
    return (1+N) * N~/2;
  }
}
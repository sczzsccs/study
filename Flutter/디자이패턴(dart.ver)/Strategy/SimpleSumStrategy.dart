import 'SumStrategy.dart';

class SimpleSumStartegy implements SumStrategy {
  @override
  int get(int N) {
    int sum = 0;
    for(int i = 0; i<=N; i++) {
      sum += i;
    }
    return sum;
  }
}
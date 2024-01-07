import 'GaussSumStrategy.dart';
import 'SimpleSumStrategy.dart';
import 'SumPrinter.dart';

void main(List<String> args) {
  SumPrinter cal = new SumPrinter();
  cal.Print(SimpleSumStartegy(), 10);
  cal.Print(GaussSumStartegy(), 10);
}
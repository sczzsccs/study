// ignore_for_file: unused_local_variable, unused_import
import 'Iterator.dart';
import 'M_Item.dart';
import 'Array.dart';

void main(List<String> args) {
  List<M_Item> items = [
    new M_Item("CPU", 1000),
    new M_Item("Keyboard", 2000),
    new M_Item("Mouse", 3000),
    new M_Item("HDD", 50)
  ];

  Array array = new Array(items);
  Iterator it = array.iterator();
  
  while(it.next()) {
    M_Item Ones = it.current();
    print(Ones.toString());
  }
}
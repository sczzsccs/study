import "ArrayIterator.dart";
import "Aggreator.dart";
import "M_Item.dart";

class Array extends Aggreator {
  List<M_Item> m_items = [];

  Array(List<M_Item> items_list) {
    this.m_items = items_list;
  }

  M_Item getItem(int idx) {
    return this.m_items[idx];
  }

  int getCount() {
    return this.m_items.length;
  }

  ArrayIterator iterator() {
    return ArrayIterator(this);
  }
}
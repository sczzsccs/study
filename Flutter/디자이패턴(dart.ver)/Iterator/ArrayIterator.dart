// ignore_for_file: unused_field
import "Array.dart";
import "Iterator.dart";

class ArrayIterator implements Iterator {
    late Array _array;
    late int _index;

    ArrayIterator(Array array) {
        this._array = array;
        this._index = -1;
    }

    @override
    bool next() {
      _index+=1;
      return _index < _array.getCount();
    }

    @override
    dynamic current() {
      return _array.getItem(_index);
    }
}
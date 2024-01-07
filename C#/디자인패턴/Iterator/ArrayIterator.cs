public class ArrayIterator : Iterator {
    private Array array;
    private int index;
    public ArrayIterator(Array array) {
        this.array = array;
        this.index = -1;
    }
    public bool next() {
        index++;
        return index < array.getCount();
    }
    public object current() {
        return array.gItem(index);
    }
}

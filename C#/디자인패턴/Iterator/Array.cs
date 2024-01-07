public class Array : Aggregator {
    private Item[] items;
    public Array(Item[] items) {
        this.items = items;
    }
    public Item gItem(int idx) {
        return items[idx];
    }
    public int getCount() {
        return items.Length;
    }

    public Iterator iterator()
    {
        return new ArrayIterator(this);
    }
}

abstract class Factory {
    protected abstract boolean isCreatable(String name);
    protected abstract Item createItem(String name);
    protected abstract void postProcessItem(String name);

    public Item create(String name) {
        boolean bCreateble = this.isCreatable(name);
        if(bCreateble) {
            Item item = this.createItem(name);
            postProcessItem(name);
            return item;
        }
        return null;
    }
}

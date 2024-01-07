public class MainEntry {
    public static void main(String[] args) {
        Factory itemFactory = new ItemFactory();
        Item item;

        item = itemFactory.create("sword");
        item = itemFactory.create("sword");
        item = itemFactory.create("sword");
        item.use();
        item.use();
        item.use();
        itemFactory.create("sword");
        itemFactory.create("sword");

        item = itemFactory.create("shield");
        item = itemFactory.create("shield");
        item.use();
        item.use();
        itemFactory.create("shield");
        item.use();
        itemFactory.create("shield");

        item = itemFactory.create("bow");
        item.use();
    }
}
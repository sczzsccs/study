import java.util.HashMap;

public class ItemFactory extends Factory {
    private class ItemData {
        int maxCount, currentCount;
        ItemData(int maxCount) {
            this.maxCount = maxCount;
        }
    }

    private HashMap<String, ItemData> repository;

    public ItemFactory() {
        repository = new HashMap<String, ItemData>();
        repository.put("sword", new ItemData(3));
        repository.put("shield", new ItemData(2));
        repository.put("bow", new ItemData(1));
    }

	@Override
	public boolean isCreatable(String name) {
        ItemData itemData = repository.get(name);
        boolean Cheak;
        if(itemData == null) {
            System.out.println(name + "은 알 수 없는 아이템입니다.");
            Cheak = false;
        }
        else if(itemData.currentCount >= itemData.maxCount) {
            System.out.println(name + "은 품절 아이템입니다.");
            Cheak = false;
        }
        else Cheak = true;
        return Cheak;
	}

	@Override
	public Item createItem(String name) {
        Item item;
        if(name == "sword") item = new Sword();
        else if(name == "shield") item = new Shield();
        else if(name == "bow") item = new Bow();
        else {
            System.out.println("error! 잘못된 아이템 이름");
            return null;
        }
        return item;
	}

	@Override
	public void postProcessItem(String name) {
        if(name == "sword") {
            repository.get(name).currentCount++; }
        else if(name == "shield") {
            repository.get(name).currentCount++; }
        else if(name == "bow") {
            repository.get(name).currentCount++; }
        else {
            System.out.println("name error!"); }
	}
}
public class TigerAdapter extends Animal {
    private Tiger tiger = new Tiger();

    public TigerAdapter(String name) {
        super(name);
        tiger.SetName(name);
    }

    @Override
    public String sound() {
        return name + " : " + tiger.roar();
    }
}
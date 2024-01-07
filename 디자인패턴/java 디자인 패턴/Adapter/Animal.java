public abstract class Animal {
    protected String name;

    protected Animal(String name) {
        this.name = name;
    }

    public abstract String sound(); 
}
public class King {
    private King() { }

    private static King self = null;

    public synchronized static King getInstance() {
        if(self == null) {
            self = new King();
        }
        return self;
    }

    public void say() {
        System.out.println("I am only one..");
    }
}
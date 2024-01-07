public class SimpleDisplay implements Display {
    public SimpleDisplay() {
        System.out.println("[Style - SimpleDisplay]");
    }

    @Override
    public void title(Draft draft) {
        System.out.println(draft.getTitle());
    }
    @Override
    public void author(Draft draft) {
        System.out.println(draft.getAuthor());
    }
    @Override
    public void content(Draft draft) {
        for (String item : draft.getContent()) {
            System.out.println(item);
        }
    }
}
public class CaptionDisplay implements Display {
    public CaptionDisplay() {
        System.out.println("[Style - CaptionDisplay]");
    }
    @Override
    public void title(Draft draft) {
        System.out.println("Title: " + draft.getTitle());
    }
    @Override
    public void author(Draft draft) {
        System.out.println("Author: " + draft.getAuthor());
    }
    @Override
    public void content(Draft draft) {
        System.out.println("Content:");
        for (String item : draft.getContent()) {
            System.out.println("\t" + item);
        }
    }
}
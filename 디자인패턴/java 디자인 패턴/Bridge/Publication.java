public class Publication extends Draft {
    private String publisher;
    private int cost;

    public Publication(String title, String author, String[] content,
        String publisher, int cost) {
        super(title, author, content);
        this.publisher = publisher;
        this.cost = cost;
    }

    public Publication(Draft draft, String publisher, int cost) {
        super(draft.getTitle(), draft.getAuthor(), draft.getContent());
        this.publisher = publisher;
        this.cost = cost;
    }

    @Override
    public void display(Display display) {
        super.display(display);
        System.out.println("#" + publisher + " $" + cost);
        System.out.println();
    }
}
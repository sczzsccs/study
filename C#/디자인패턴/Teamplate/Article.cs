public class Article
{
    private String title;
    private List<String> content;
    private String footer;

    public Article(string title, List<string> content, string footer)
    {
        this.title = title;
        this.content = content;
        this.footer = footer;
    }

    public String getTitle() { return title; }
    public List<String> getContent() { return content; }
    public String getFooter() { return footer; }
}
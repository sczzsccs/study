public class CaptionDisplayArticle : DisplayArticleTemplate
{
    public CaptionDisplayArticle(Article article) : base(article)
    { }

    protected override void title()
    {
        Console.WriteLine("Title: " + article.getTitle());
    }

    protected override void content()
    {
        Console.WriteLine("Content:");
        foreach (String contentItem in article.getContent())
        {
            Console.WriteLine("\t" + contentItem);
        }
    }

    protected override void footer()
    {
        Console.WriteLine("Footer: " + article.getFooter());
    }
}
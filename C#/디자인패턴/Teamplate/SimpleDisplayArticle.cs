public class SimpleDisplayArticle : DisplayArticleTemplate
{
    public SimpleDisplayArticle(Article article) : base(article)
    {
    }

    protected override void title()
    {
        Console.WriteLine(article.getTitle());
    }

    protected override void content()
    {
        foreach (String contentItem in article.getContent())
        {
            Console.WriteLine(contentItem);
        }
    }

    protected override void footer()
    {
        Console.WriteLine(article.getFooter());
    }
}
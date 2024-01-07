public abstract class DisplayArticleTemplate
{
    protected Article article;
    protected abstract void title();
    protected abstract void content();
    protected abstract void footer();

    protected DisplayArticleTemplate(Article article)    
    {
        this.article = article;
    }

    public void display()
    {
        title();
        content();
        footer();
    }
}
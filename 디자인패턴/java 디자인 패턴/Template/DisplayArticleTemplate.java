public abstract class DisplayArticleTemplate {
    protected Article article;
    protected abstract void title();
    protected abstract void content();
    protected abstract void footer();

    public DisplayArticleTemplate(Article article) {
        this.article = article;
    }

    public final void display() {
        title();
        content();
        footer();
    }
}
import java.util.ArrayList;

public class SimpleDisplayArticle extends DisplayArticleTemplate {
    public SimpleDisplayArticle(Article article) {
        super(article);
    }

    @Override
    protected void title() {
        System.out.println(article.getTitle());
    }

    @Override
    protected void content() {
        ArrayList<String> content = article.getcontent();
        int CntLines = content.size();
        for (int i=0; i<CntLines; i++) {
            System.out.println(content.get(i));
        }
    }

    @Override
    protected void footer() {
        System.out.println(article.getfooter());
    }
}

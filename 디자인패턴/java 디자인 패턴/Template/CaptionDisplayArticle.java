import java.util.ArrayList;

public class CaptionDisplayArticle extends DisplayArticleTemplate {
    public CaptionDisplayArticle(Article article) {
        super(article);
    }

    @Override
    protected void title() {
        System.out.println("Title: " + article.getTitle());
    }

    @Override
    protected void content() {
        System.out.println("Content:");
        
        ArrayList<String> content = article.getcontent();
        int CntLines = content.size();
        for (int i=0; i<CntLines; i++) {
            System.out.println("\t" + content.get(i));
        }
    }

    @Override
    protected void footer() {
        System.out.println("Footer: " + article.getfooter());
    }
}

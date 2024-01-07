import java.util.ArrayList;

public class MainEntry {
    public static void main(String[] args) {
        String Title = "디자인패턴";

        ArrayList<String> Content = new ArrayList<String>();
        Content.add("디자인패턴은 클래스 간의 효율적이고 최적화된 관계를 설계하는 것입니다.");
        Content.add("각 패턴을 외우기 보다 이해하는 것이 중요합니다.");
        Content.add("다양한 패턴을 접하고 반복적으로 이해할수록");
        Content.add("각 디자인패턴에 대한 응용의 폭이 넓어질 것입니다.");

        String Footer = "2022.01.09, GIS Developer 김형준";


        Article article = new Article(Title, Content, Footer);

        System.out.println("[STYLE - SimpleDisplayArticle]");
        DisplayArticleTemplate style1 = new SimpleDisplayArticle(article);
        style1.display();
        System.out.println();

        System.out.println("[STYLE - CaptionDisplayArticle]");
        DisplayArticleTemplate style2 = new CaptionDisplayArticle(article);
        style2.display();
    }
}
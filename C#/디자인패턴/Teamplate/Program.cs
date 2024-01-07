internal class Program
{
    static void Main(string[] args)
    {
        String Title = "디자인패턴";
        List<string> Content = new List<string>();
        Content.Add("디자인패턴은 클래스 간의 효율적이고 최적화된 관계를 설계하는 것입니다.");
        Content.Add("각 패턴을 외우기 보다 이해하는 것이 중요합니다.");
        Content.Add("다양한 패턴을 접하고 반복적으로 이해할수록");
        Content.Add("각 디자인패턴에 대한 응용의 폭이 넓어진 것입니다.");
        String Footer = "2022.01.09, GIS Devleoper 김형준";

        Article article = new Article(title:Title, content:Content, footer:Footer);

        Console.WriteLine("[STYLE - SimpleDisplayArticle]");
        DisplayArticleTemplate style1 = new SimpleDisplayArticle(article);
        style1.display();
        Console.WriteLine();

        Console.WriteLine("[STYLE - CaptionDisplayArticle]");
        DisplayArticleTemplate style2 = new CaptionDisplayArticle(article);
        style2.display();
        Console.WriteLine();
    }
}
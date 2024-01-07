public class MainEntry {
    public static void main(String[] args) {
        String Title = "제목";
        String Author = "저자";
        String[] Content = { 
            "내용1", 
            "내용2", 
            "내용3"
        };

        Draft draft = new Draft(Title, Author, Content);
        draft.display(new SimpleDisplay());
        draft.display(new CaptionDisplay());


        var Publisher = "북악출판";
        var cost = 100;
        Publication publi = new Publication(draft, Publisher, cost);
        publi.display(new SimpleDisplay());
        publi.display(new CaptionDisplay());
    }
}
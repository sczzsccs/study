public class MainEntry {
    public static void main(String[] args) {
        King king = King.getInstance();
        king.say();

        King king2 = king.getInstance();
        
        if(king == king2) {
            System.out.println("seam object");
        }
        else {
            System.out.println("different object");
        }
    }
}
public class ex02 {
    static class Box {
        private int a, b;

        public Box(int a, int b) {
            if(a>0 && b>0) {
                this.a = a;
                this.b = b;
            }
            else {
                this.a = -a;
                this.b = -b;
            }
        }

        public void Print() {
            System.out.println(this.a + this.b);
        }
    }

    public static void main(String[] args) {
        Box box = new Box(10, 10);
        box.Print();
        
        box = new Box(-10, 10);
        box.Print();
    }
}
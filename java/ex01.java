import java.util.Arrays;

class ex01 {
    public class Test {
        static void test(String[] args) {
            main(new String[] {"zz"});
        }
    }

    public static void main(String[] args) {
        ex01.Test.test(args);
        System.out.println(Arrays.toString(args));
    }
}
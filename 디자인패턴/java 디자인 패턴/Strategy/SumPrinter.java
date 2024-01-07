public class SumPrinter {
    void print(SumStrategy stratgy, int N) {
        System.out.printf("The Sum of 1 - %d : ", N);
        System.out.println(stratgy.get(N));
    }
}
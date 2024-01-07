import java.util.Arrays;

public class Binary_search {
    static int binary_search(int n, int[] array) {
        Arrays.sort(array);
        int Mid = array.length/2;
        while (array[Mid] != n) {
            if (array[Mid] > n) {
                Mid /= 2;
            } else {
                Mid += (Mid/2);
            }
        }
        return array[Mid];
    }
    
    public static void main(String[] args) {
        int[] array = new int[] {9,1,4,7,3};
        System.out.println(binary_search(7,array));
    }
}
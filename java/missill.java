import java.util.Arrays;
import java.util.Comparator;

public class missill {
    public static int solution(int[][] targets) {
        // 첫번째 숫자 기준 오름차순 정렬
        Arrays.sort(targets, Comparator.comparing(o1 -> o1[0]));
        int answer = 1;
        int end = targets[0][1];
        for (int i = 1; i < targets.length; i++) {
            if (end <= targets[i][0]) {
                answer++; // new group
                end = targets[i][1];
                continue;
            } else if (end > targets[i][1]) {
                end = targets[i][1]; // end updata
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        TestCase Case = new TestCase();

        int[][] missill = new int[][]{{5, 11}, {10, 23}, {4, 6}, {13, 17}, {11, 15}, {8, 10}, {4, 24}, {5, 12}, {7, 22}, {14, 15}, {14, 24}, {5, 6}, {18, 19}};
        System.out.println("{{5, 11}, {10, 23}, {4, 6}, {13, 17}, {11, 15}, {8, 10}, {4, 24}, {5, 12}, {7, 22}, {14, 15}, {14, 24}, {5, 6}, {18, 19}}");
        System.out.println("내 코드 테스트결과: "+solution(missill));
        System.out.println();

        missill = new int[][]{{4, 5}, {4, 8}, {10, 14}, {11, 13}, {5, 12}, {3, 7}, {1, 4}};
        System.out.println("{{4, 5}, {4, 8}, {10, 14}, {11, 13}, {5, 12}, {3, 7}, {1, 4}}");
        System.out.println("내 코드 테스트결과: "+solution(missill));
    }
}
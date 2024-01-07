package 소트인사이드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class MainEntry {
    public static void main(String[] args) throws IOException {
        // !문제
        // *배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
        // 입력
        // *첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
        // 출력
        // *첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

        // TODO 1       TODO 2        TODO 3            TODO 4
        // 예제 입력 1  예제 입력 2     예제 입력 3     예제 입력 4 
        // 2143         999998999       61423           500613009
        // 예제 출력 1  예제 출력 2     예제 출력 3     예제 출력 4 
        // 4321         999999998       64321           965310000
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] input =  br.readLine().toCharArray();
        Arrays.sort(input);
        System.out.println(new StringBuilder(new String(input)).reverse().toString());
    }
}
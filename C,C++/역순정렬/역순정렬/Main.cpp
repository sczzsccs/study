//#define _CRT_SECURE_NO_WARNINGS
//#include <stdio.h>
//#include <corecrt_malloc.h>
//
//void main() {
//	/*각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다.
//	* 앞으로 M번 바구니의 순서를 역순으로 만들려고 한다.
//	* 한 번 순서를 역순으로 바꿀 때, 순서를 역순으로 만들 범위를 정하고, 그 범위에 들어있는 바구니의 순서를 역순으로 만든다.
//	* 바구니의 순서를 어떻게 바꿀지 주어졌을 때, M번 바구니의 순서를 역순으로 만든 다음, 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램
//	* 
//	* 
//	*입력
//		첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
//		둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다.
//		방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. (1 ≤ i ≤ j ≤ N)
//		입력으로 주어진 순서대로 바구니의 순서를 바꾼다.
//	*/
//
//	int* array;
//	int n, m;
//	int i, j, temp;
//	printf("index:");
//	scanf("%d %d", &n, &m);
//	array = (int*)malloc(sizeof(int) * n);
//	for (int i = 1; i <= n; i++) {
//		array[i-1] = i;
//		printf("%d ", array[i - 1]);
//	}
//	printf("\n");
//	for (int k = 0; k < m; k++)
//	{
//		scanf("%d %d", &i, &j);
//		i -= 1, j -= 1;
//		printf("i:%d, j:%d\n", array[i], array[j]);
//		for (int l = 0; l <= (j - i) / 2; l++) {
//			temp = array[i+l];
//			array[i+l] = array[j-l];
//			printf("t:%d, j+l:%d\n", temp, array[j - l]);
//			array[j-l] = temp;
//			printf("%d:%d, %d:%d\n", i + l, array[i + l], j - l, array[j - l]);
//		}
//		for (int i = 0; i < n; i++) {
//			printf("%d ", array[i]);
//		}
//		printf("\n");
//	}
//	for (int i = 0; i < n; i++) { 
//		printf("%d ", array[i]);
//	}
//}

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int array[100];
	int n, m;
	int i, j, temp;

	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; i++) {
		array[i - 1] = i;
	}

	for (int k = 0; k < m; k++) {
		scanf("%d %d", &i, &j);
		i -= 1, j -= 1;
		for (int l = 0; l <= (j - i) / 2; l++) {
			temp = array[i + l];
			array[i + l] = array[j - l];
			array[j - l] = temp;
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d ", array[i]);
	}
	return 0;
}
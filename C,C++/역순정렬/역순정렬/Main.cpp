//#define _CRT_SECURE_NO_WARNINGS
//#include <stdio.h>
//#include <corecrt_malloc.h>
//
//void main() {
//	/*������ �ٱ��Ͽ��� 1������ N������ ��ȣ�� ������� ������ �ִ�.
//	* ������ M�� �ٱ����� ������ �������� ������� �Ѵ�.
//	* �� �� ������ �������� �ٲ� ��, ������ �������� ���� ������ ���ϰ�, �� ������ ����ִ� �ٱ����� ������ �������� �����.
//	* �ٱ����� ������ ��� �ٲ��� �־����� ��, M�� �ٱ����� ������ �������� ���� ����, �ٱ��Ͽ� �����ִ� ��ȣ�� ���� ���� �ٱ��Ϻ��� ����ϴ� ���α׷�
//	* 
//	* 
//	*�Է�
//		ù° �ٿ� N (1 �� N �� 100)�� M (1 �� M �� 100)�� �־�����.
//		��° �ٺ��� M���� �ٿ��� �ٱ����� ������ �������� ����� ����� �־�����.
//		����� i j�� ��Ÿ����, �������κ��� i��° �ٱ��Ϻ��� j��° �ٱ����� ������ �������� ����ٴ� ���̴�. (1 �� i �� j �� N)
//		�Է����� �־��� ������� �ٱ����� ������ �ٲ۴�.
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
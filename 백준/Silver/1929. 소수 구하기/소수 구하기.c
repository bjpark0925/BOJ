#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int main() {

	int m, n, flag = 1;

	scanf("%d %d", &m, &n);
	int* arr = (int*)malloc(sizeof(int) * (n + 1));
	for (int i = m; i <= n; i++) {
		arr[i] = 1;
	}
	arr[1] = 0;

	for (int i = 2; i*i <= n; i++) {
		for (int j = i * i; j <= n; j += i) {
			arr[j] = 0;
		}
	}

	for (int i = m; i <= n; i++)
		if (arr[i] == 1)
			printf("%d\n", i);


	return 0;
}
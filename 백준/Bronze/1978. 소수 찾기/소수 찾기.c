#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int main() {

	int n, cnt = 0, max = 0;
	int* Narr= (int*)malloc(sizeof(int) * 100);
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int num;
		//Narr = (int*)malloc(sizeof(int) * n);

		scanf("%d", &num);
		Narr[i] = num;
		if (max < num)
			max = num;
	}

	int* Parr = (int*)malloc(sizeof(int) * (max + 1));
	for (int j = 0; j <= max; j++)
		Parr[j] = 0;
	Parr[1] = 1;

	for (int j = 2; j * j <= max; j++) {
		for (int k = j * j; k <= max; k += j) {
			Parr[k] = 1;
		}
	}

	for (int i = 0; i < n; i++) {
		if (Parr[Narr[i]] == 0)
			cnt++;
	}

	printf("%d", cnt);


	return 0;
}
#pragma warning(disable: 4996)
#include<stdio.h>
#include<stdlib.h>//malloc
#define SIZE 3

int main() {

	int* arr = (int*)malloc(sizeof(int) * SIZE);

	while (1) {
		scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);
		if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0)
			break;
		for (int i = 0; i < SIZE - 1; i++) {
			if (arr[i] > arr[i + 1]) {
				int temp = arr[i];
				arr[i] = arr[i + 1];
				arr[i + 1] = temp;
			}
		}
		if (arr[2] * arr[2] == (arr[0] * arr[0]) + (arr[1] * arr[1]))
			printf("right\n");
		else
			printf("wrong\n");
	}

	return 0;
}
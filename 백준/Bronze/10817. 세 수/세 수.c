#pragma warning(disable: 4996)
#include<stdio.h>

void bubble_sort(int arr[]) {
	int temp;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 2; j++) {
			if (arr[j] > arr[j + 1]) {
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

int main() {

	int a[3];
	
	scanf("%d %d %d", &a[0], &a[1], &a[2]);

	bubble_sort(a);

	printf("%d", a[1]);

	return 0;
}
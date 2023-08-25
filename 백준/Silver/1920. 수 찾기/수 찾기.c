#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int binarySearch(int *arr, int size, int num)
{
	int left = 0;
	int right = size;
	int mid;

	while (left <= right) {
		mid = (left + right) / 2;

		if (arr[left] == num)
			return 1;
		if (arr[right] == num)
			return 1;

		if (arr[mid] == num)
			return 1;
		else if (arr[mid] < num)
			left = mid + 1;
		else
			right = mid - 1;
	}

	return 0;
}

int compare(const void* a, const void* b)
{
	if (*(int*)a > *(int*)b)
		return 1;
	else {
		if (*(int*)a < *(int*)b)
			return -1;
		else
			return 0;
	}
}

int main() {

	int n, m, tmp, flag = 0;

	scanf("%d", &n);
	int* Narr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &Narr[i]);
	}

	//qsort
	qsort(Narr, n, sizeof(int), compare);

	scanf("%d", &m);
	int* answer = (int*)malloc(sizeof(int) * m);
	for (int i = 0; i < m; i++) {
		scanf("%d", &tmp);
		flag = binarySearch(Narr, n - 1, tmp);
		answer[i] = flag;
		flag = 0;
	}

	for (int i = 0; i < m; i++)
		printf("%d\n", answer[i]);


	return 0;
}
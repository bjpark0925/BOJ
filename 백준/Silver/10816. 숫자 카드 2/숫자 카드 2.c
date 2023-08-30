#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>//malloc

int compare(const void* a, const void* b)
{
	int n1 = *(int*)a;
	int n2 = *(int*)b;

	if (n1 < n2)
		return -1;

	if (n1 > n2)
		return 1;

	return 0;
}

int lower_bound(int* own, int size, int key)
{
	int left = 0;
	int right = size - 1;
	while (left < right) {
		int mid = (left + right) / 2;
		if (own[mid] >= key)
			right = mid;
		else
			left = mid + 1;
	}

	if (own[right] == key)
		return right;
	else
		return 0;
}

int upper_bound(int* own, int size, int key)
{
	int left = 0;
	int right = size;

	while (left < right) {
		int mid = (left + right) / 2;
		if (own[mid] > key)
			right = mid;
		else
			left = mid + 1;
	}

	if (own[right - 1] == key)
		return right;
	else
		return 0;
}

int main() {
	int n, m;
	scanf("%d", &n);
	int* own = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
		scanf("%d", &own[i]);

	scanf("%d", &m);
	int* num = (int*)malloc(sizeof(int) * m);
	for (int i = 0; i < m; i++)
		scanf("%d", &num[i]);

	qsort(own, n, sizeof(int), compare);
	for (int i = 0; i < m; i++) {
		printf("%d ", upper_bound(own, n, num[i]) - lower_bound(own, n, num[i]));
	}

	return 0;
}
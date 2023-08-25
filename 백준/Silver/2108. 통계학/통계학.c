#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

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
	int n;
	scanf("%d", &n);
	int* arr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		int num;
		scanf("%d", &num);
		arr[i] = num;
	}

	qsort(arr, n, sizeof(int), compare);

	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += arr[i];
	}
	double avg = (double)sum / n;
	//반올림
	int mean;
	if (avg > 0)
		mean = (int)(avg + 0.5);
	else
		mean = (int)(avg - 0.5);

	int cnt = 1;
	int max_cnt = 1;
	int mode_cnt = 0;
	int mode = arr[0];
	for (int i = 0; i < n - 1; i++) {
		if (arr[i] == arr[i + 1]) {
			cnt++;
			if (i != n - 2)
				continue;
		}

		if (cnt == max_cnt) {
			mode_cnt++;
			if (mode_cnt == 2)
				mode = arr[i];
			cnt = 1;
		}

		else if (cnt > max_cnt) {
			max_cnt = cnt;
			cnt = 1;
			mode_cnt = 1;
			mode = arr[i];
		}

		else
			cnt = 1;
	}

	int median = arr[(n - 1) / 2];

	int range = arr[n - 1] - arr[0];

	printf("%d\n%d\n%d\n%d\n", mean, median, mode, range);

	return 0;
}
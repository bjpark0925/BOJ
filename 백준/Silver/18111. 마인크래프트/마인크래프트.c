#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>//malloc
#include<limits.h>//int_max

int main() {
	int n, m, b;
	scanf("%d %d %d", &n, &m, &b);
	int** arr = (int**)malloc(sizeof(int*) * n);
	for (int i = 0; i < n; i++)
		arr[i] = (int*)malloc(sizeof(int) * m);

	int max = 0;
	int min = 256;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) {
			scanf(" %d", &arr[i][j]);
			if (max < arr[i][j])
				max = arr[i][j];
			if (min > arr[i][j])
				min = arr[i][j];
		}

	int min_time = INT_MAX;
	int h = 0;
	for (int height = max; height >= min; height--) {
		int time = 0;
		int inventory = b;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				int diff = height - arr[i][j];
				if (diff > 0) {//블록 쌓기
					time += diff;
					inventory -= diff;
				}
				else if (diff < 0) {//블록 빼기
					//diff가 음수인 것 주의
					time -= 2 * diff;
					inventory -= diff;
				}
			}
		}

		if (inventory < 0)
			continue;
		if (min_time > time) {
			min_time = time;
			h = height;
		}
	}

	printf("%d %d\n", min_time, h);

	for (int i = 0; i < n; i++)
		free(arr[i]);
	free(arr);

	return 0;
}
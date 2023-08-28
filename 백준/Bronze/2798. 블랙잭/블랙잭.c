#pragma warning(disable: 4996)
#include<stdio.h>
#include<stdlib.h>//malloc

int main() {
	int n, m;
	scanf("%d %d", &n, &m);

	int* arr = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	int max = 0;
	for (int x = 0; x < n - 2; x++) {
		for (int y = x + 1; y < n - 1; y++) {
			for (int z = y + 1; z < n; z++) {
				int sum = arr[x] + arr[y] + arr[z];

				if (sum > m)
					continue;

				if (max < sum)
					max = sum;
			}
		}
	}

	printf("%d\n", max);

	return 0;
}
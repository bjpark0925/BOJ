#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int main() {

	int k, n;
	scanf("%d %d", &k, &n);

	long long* arr = (long long*)malloc(sizeof(long long) * k);
	long long sum = 0;
	for (int i = 0; i < k; i++) {
		scanf("%lld", &arr[i]);
		sum += arr[i];
	}

	long long right = sum / k;
	long long left = 1;
	long long cnt = 0;
	while (left <= right) {
		long long mid = (left + right) / 2;
		for (int i = 0; i < k; i++) {
			cnt += arr[i] / mid;
		}

		if (cnt < n) {
			right = mid - 1;
		}

		else {
			left = mid + 1;
		}

		cnt = 0;
	}

	printf("%lld\n", right);

	return 0;
}
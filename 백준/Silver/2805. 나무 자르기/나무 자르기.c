#pragma warning(disable: 4996)
#include<stdio.h>
#include<stdlib.h>//malloc

int main() {
	long long n, m;
	long long max = 0;
	scanf("%lld %lld", &n, &m);

	long long* arr = (long long*)malloc(sizeof(long long) * n);
	for (long long i = 0; i < n; i++) {
		scanf("%lld", &arr[i]);
		if (arr[i] > max)
			max = arr[i];
	}

	long long left = 0, right = max;
	long long height = 0;

	while (left<=right) {
		long long mid = (left + right) / 2;
		long long sum = 0;
		int flag = 0;
		for (long long i = 0; i < n; i++) {
			if (arr[i] <= mid)
				continue;
			sum += arr[i] - mid;
		}

		if (sum == m) {
			height = mid;
			break;
		}
		else if (sum > m)
			left = mid + 1;
		else {
			right = mid - 1;
			flag = 1;
		}

		if (left > right)
			if (flag == 1)
				height = mid - 1;
			else
				height = mid;
	}

	printf("%lld\n", height);

	return 0;
}
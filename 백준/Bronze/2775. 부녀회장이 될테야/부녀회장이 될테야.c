#pragma warning(disable:4996)
#include<stdio.h>

int House(int k, int n)
{
	if (k == 0)
		return n;
	if (n == 1)
		return 1;

	return House(k, n - 1) + House(k - 1, n);
}

int main() {
	int t;
	scanf("%d", &t);

	while (t > 0) {
		int k, n;
		scanf("%d", &k);
		scanf("%d", &n);

		printf("%d\n", House(k, n));

		t--;
	}

	return 0;
}
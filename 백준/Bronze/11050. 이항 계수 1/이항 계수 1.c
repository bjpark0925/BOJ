#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int main() {
	int n;
	int k;
	int c = 1;
	scanf("%d %d", &n, &k);

	for (int i = 0; i < k; i++) {
		c = c * n;
		n--;
	}

	for (int i = k; i > 0; i--) {
		c = c / i;
	}

	printf("%d\n", c);

	return 0;
}
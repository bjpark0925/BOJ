#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int main() {

	int n, sum = 1, cnt = 1;
	scanf("%d", &n);

	while (1) {
		if (sum >= n) {
			break;
		}

		sum += 6 * cnt;
		cnt++;
	}

	printf("%d\n", cnt);

	return 0;
}
#pragma warning(disable:4996)
#include<stdio.h>
int main() {

	int n, i, j;

	scanf("%d", &n);

	for (i = 0; i < 2*n-1; i++) {
		if (i < n-1) {
			for (j = n - 1; j > 0; j--) {
				if (j > i)
					printf(" ");
				else
					printf("*");
			}
			for (j = 0; j < n; j++) {
				if (j <= i)
					printf("*");
			}
		}
		else {
			for (j =0; j <n-1; j++) {
				if (j>i-n)
					printf("*");
				else
					printf(" ");
			}
			for (j = 0; j < n; j++) {
				if (j > i - n)
					printf("*");
			}
		}
		printf("\n");
	}

	return 0;
}
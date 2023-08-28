#pragma warning(disable:4996)
#include<stdio.h>
int main() {

	int n, i, j;

	scanf("%d", &n);

	for (i = 0; i < n; i++) {
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
		printf("\n");
	}

	return 0;
}
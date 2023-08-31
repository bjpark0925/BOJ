#pragma warning(disable:4996)
#include <stdio.h>
int main() {

	int n, i, j;

	scanf("%d", &n);

	
	for (i = 0; i < n; i++) {
		for (j = n-i; j >1; j--) {
			printf(" ");
		}
		for (j = 0; j <= i; j++) {
			if (n == 1) {
				printf("*");
                return 0;
			}
			printf("* ");
		}
		if (i == n-1)
			continue;
		printf("\n");
	}
	
	return 0;
}
#pragma warning(disable:4996)
#include <stdio.h>
int main() {

	int n;

	scanf("%d", &n);

	
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= 2 * n; j++) {
			if (i % 2 != 0) {
				if (j % 2 != 0)
					printf("*");
				else
					printf(" ");
			}
			else {
				if (j % 2 == 0)
					printf("*");
				else
					printf(" ");
			}
		}
		if (i == n)
			continue;
		printf("\n");
	}
	
	return 0;
}
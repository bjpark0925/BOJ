#pragma warning(disable:4996)
#include <stdio.h>
int main() {

	int n, i;

	scanf("%d", &n);

	for (i = n-1; i > 0; i--) {
		n *= i;
	}
	if (n == 0)
		n = 1;

	printf("%d", n);

	return 0;
}
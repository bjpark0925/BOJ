#pragma warning(disable:4996)
#include <stdio.h>
int main() {

	int A, B, a, b, r, max, min;

	scanf("%d %d", &A, &B);

	a = A;
	b = B;

	while (b != 0) {
		r = a % b;
		a = b;
		b = r;
	}
	max = a;

	min = A * B / max;

	printf("%d\n%d", max, min);

	return 0;
}
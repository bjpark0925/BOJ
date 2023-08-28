#pragma warning(disable: 4996)
#include<stdio.h>

int main() {

	int a, b, v;

	scanf("%d %d %d", &a, &b, &v);

	if ((v - b) % (a - b) == 0)
		printf("%d\n", (v - b) / (a - b));
	else
		printf("%d\n", (v - b) / (a - b) + 1);

	return 0;
}
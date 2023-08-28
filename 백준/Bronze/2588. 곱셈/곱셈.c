#pragma warning(disable:4996)
#include<stdio.h>
int main() {

	int a, b;
	int b1, b2, b3;
	int ans1, ans2, ans3, result;

	scanf("%d %d", &a, &b);

	b1 = b % 10;
	b2 = (b % 100 - b1)/10;
	b3 = b / 100;

	ans1 = b1 * a;
	ans2 = b2 * a;
	ans3 = b3 * a;

	result = ans1 + 10 * ans2 + 100 * ans3;

	printf("%d\n%d\n%d\n%d", ans1, ans2, ans3, result);


	return 0;
}
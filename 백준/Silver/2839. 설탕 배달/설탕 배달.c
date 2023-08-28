#pragma warning(disable: 4996)
#include<stdio.h>

int main() {

	int n;
	scanf("%d", &n);

	int b3 = 0, b5 = 0;
	int flag = 0;

	while (n >= 3) {
		if (n % 5 == 0) {
			b5 += n / 5;
			flag = 1;
			break;
		}
		else {
			n -= 3;
			b3++;
		}
	}

	if (n == 0 || flag == 1)
		printf("%d\n", b3 + b5);
	else
		printf("%d\n", -1);
		

	return 0;
}
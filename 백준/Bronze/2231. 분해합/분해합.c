#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int main() {

	int n, ctor;
	int flag = 0;
	scanf("%d", &n);

	for (int i = 1; i < n; i++) {
		int sum = i;
		int tmp = i;

		while (tmp > 0) {
			sum += tmp % 10;
			tmp = tmp / 10;
		}
		if (sum == n) {
			flag = 1;
			ctor = i;
			break;
		}
	}
	
	if (flag == 0)
		printf("0\n");

	else
		printf("%d\n", ctor);


	return 0;
}
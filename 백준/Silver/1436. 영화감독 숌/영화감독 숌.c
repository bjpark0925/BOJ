#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int main() {
	int N;
	scanf("%d", &N);

	int num = 666;
	int six_cnt = 0;
	int num_cnt = 0;

	while (1) {
		int tmp = num;
		while (tmp != 0) {
			if (six_cnt >= 3)
				break;

			if (tmp % 10 == 6)
				six_cnt++;
			else
				six_cnt = 0;
			tmp = tmp / 10;
		}

		if (six_cnt>=3)
			num_cnt++;

		if (num_cnt == N) {
			printf("%d\n", num);
			break;
		}

		six_cnt = 0;
		num++;
	}

	return 0;
}
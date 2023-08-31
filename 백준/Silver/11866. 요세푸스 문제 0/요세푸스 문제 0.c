#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>//malloc

int main() {
	int n, k;
	scanf("%d %d", &n, &k);

	int* flag = (int*)malloc(sizeof(int) * (n + 1));
	for (int i = 0; i < n + 1; i++)
		flag[i] = 0;

	printf("<");

	int cur = 0;
	int flag_cnt = 0;
	int cur_cnt = 0;

	while (flag_cnt < n) {
		if (cur_cnt == k) {
			if (flag_cnt == n - 1)
				printf("%d>", cur);
			else
				printf("%d, ", cur);
			flag[cur]++;
			flag_cnt++;
			cur_cnt = 0;
		}
		if (cur == n) {
			cur = 0;
		}

		cur++;
		if (flag[cur] != 0)
			continue;
		cur_cnt++;
	}

	return 0;
}
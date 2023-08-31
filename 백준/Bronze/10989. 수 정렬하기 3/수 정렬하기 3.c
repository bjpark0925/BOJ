#pragma warning(disable: 4996)
#include<stdio.h>
#include<stdlib.h>//malloc
#define MAX 10001

int cnt[MAX] = { 0, };

int main() {
	int n, num;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &num);
		cnt[num]++;
	}

	for (int i = 0; i <= MAX; i++) {
		if (cnt[i] == 0)
			continue;
		for (int j = 0; j < cnt[i]; j++)
			printf("%d\n", i);
	}

	return 0;
}
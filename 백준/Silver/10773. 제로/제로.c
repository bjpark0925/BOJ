#pragma warning(disable: 4996)
#include<stdio.h>
#include<stdlib.h>//malloc

int main() {
	int k;
	scanf("%d", &k);
	int* s = (int*)malloc(sizeof(int) * k);
	int s_top = -1;

	for (int i = 0; i < k; i++) {
		int tmp;
		scanf("%d", &tmp);
		if (tmp == 0)
			s_top--;
		else {
			s_top++;
			s[s_top] = tmp;
		}
	}

	if (s_top == -1)
		printf("%d\n", 0);
	else {
		int sum = 0;
		for (int i = 0; i <= s_top; i++)
			sum += s[i];
		printf("%d\n", sum);
	}

	return 0;
}
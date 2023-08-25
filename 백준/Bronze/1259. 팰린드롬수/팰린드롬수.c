#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

//팰린드롬수 최대 5자리
int main() {

	int i = 0;
	int j = 0;
	int flag = 0;
	int num, len;
	int arr[5] = { 0 };

	while (1) {
		scanf("%d", &num);
		if (num == 0)
			break;

		while (num != 0) {
			arr[i] = num % 10;
			num = num / 10;
			i++;
		}
		len = i;
		i--;

		while (j <= i) {
			if (arr[j] != arr[i])
				flag = 1;
			j++;
			i--;
		}

		if (flag == 0)
			printf("yes\n");
		else
			printf("no\n");

		//재사용 위해 초기화
		for (int k = 0; k < len; k++)
			arr[k] = 0;

		i = 0;
		j = 0;
		flag = 0;
	}

	return 0;
}
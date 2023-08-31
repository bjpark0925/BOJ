#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>//malloc

int main() {
	int l;
	long long r = 1, M = 1234567891;
	scanf("%d", &l);
	char* a = (char*)malloc(sizeof(char) * (l + 1));
	scanf("%s", a);

	long long hash = 0;
	for (int i = 0; i < l; i++) {
		hash = (hash + (a[i] - 'a' + 1) * r) % M;
		r = (r * 31) % M;
	}

	printf("%lld\n", hash);

	return 0;
}
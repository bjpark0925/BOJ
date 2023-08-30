#pragma warning(disable:4996)
#include<stdio.h>

int main() {
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		int h, w, n;
		scanf("%d %d %d", &h, &w, &n);
		int height = n % h, width = (n / h) + 1;
		if (height == 0) {
			height = h;
			width--;
		}
			
		printf("%d\n", (height * 100) + width);
	}

	return 0;
}
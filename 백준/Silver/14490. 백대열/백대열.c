#pragma warning(disable:4996)
#include<stdio.h>
int main() {

	int n, m;
	int n1, m1;
	int temp, r;

	scanf("%d:%d", &n, &m);

	n1 = n;
	m1 = m;

	if (n > m) {
		while (m!=0) {
			r = n % m;
			n = m;
			m = r;		
		}
		printf("%d:%d", n1 / n, m1 / n);
	}
	else {
		while (n!=0) {
			r = m % n;
			m = n;
			n = r;
		}
		printf("%d:%d", n1 / m, m1 / m);
	}
	

	return 0;
}
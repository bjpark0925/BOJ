#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>//malloc

typedef struct {
	int x;
	int y;
}grid;

int compare(const void* a, const void* b)
{
	grid a1 = *(grid*)a;
	grid a2 = *(grid*)b;

	if (a1.y < a2.y)
		return -1;

	else if (a1.y > a2.y)
		return 1;

	else {
		if (a1.x > a2.x)
			return 1;
		else
			return -1;
	}

	return 0;
}

int main() {
	int n;
	scanf("%d", &n);
	grid* g = (grid*)malloc(sizeof(grid) * n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &g[i].x, &g[i].y);
	}

	qsort(g, n, sizeof(grid), compare);

	for (int i = 0; i < n; i++) {
		printf("%d %d\n", g[i].x, g[i].y);
	}

	free(g);

	return 0;
}
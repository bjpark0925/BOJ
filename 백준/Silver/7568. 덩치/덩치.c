#pragma warning(disable: 4996)
#include<stdio.h>
#include<stdlib.h>//malloc
typedef struct {
	int weight;
	int height;
	int rank;
}Shape;

int main() {
	int n;
	scanf("%d", &n);

	Shape* s = (Shape*)malloc(sizeof(Shape) * n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &s[i].weight, &s[i].height);
		s[i].rank = 1;
	}

	for (int i = 0; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			if (s[i].weight < s[j].weight && s[i].height < s[j].height)
				s[i].rank++;
			else if (s[i].weight > s[j].weight && s[i].height > s[j].height)
				s[j].rank++;
		}
	}

	for (int i = 0; i < n; i++)
		printf("%d ", s[i].rank);


	return 0;
}
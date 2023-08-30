#pragma warning(disable: 4996)
#include<stdio.h>
#include<stdlib.h>//malloc
#define MAX 101

typedef struct {
	int age;
	char name[MAX];
}Member;

void Merge(Member* m, int start, int end)
{
	int mid = (start + end) / 2;
	int left = start;
	int right = mid;
	Member* temp = (Member*)malloc(sizeof(Member) * end);

	for (int i = start; i < end; i++) {
		if (left == mid) {
			temp[i].age = m[right].age;
			strcpy(temp[i].name, m[right].name);
			right++;
		}
		else if (right == end) {
			temp[i].age = m[left].age;
			strcpy(temp[i].name, m[left].name);
			left++;
		}
		else if (m[left].age <= m[right].age) {
			temp[i].age = m[left].age;
			strcpy(temp[i].name, m[left].name);
			left++;
		}
		else {
			temp[i].age = m[right].age;
			strcpy(temp[i].name, m[right].name);
			right++;
		}
	}

	for (int i = start; i < end; i++) {
		m[i].age = temp[i].age;
		strcpy(m[i].name, temp[i].name);
	}

	free(temp);
}

void Sort(Member* m, int start, int end)
{
	if (start + 1 == end)
		return;

	int mid = (start + end) / 2;

	Sort(m, start, mid);
	Sort(m, mid, end);

	Merge(m, start, end);
}

int main() {
	int n;
	scanf("%d", &n);
	Member* m = (Member*)malloc(sizeof(Member) * n);
	for (int i = 0; i < n; i++)
		scanf("%d %s", &m[i].age, m[i].name);

	Sort(m, 0, n);

	for (int i = 0; i < n; i++)
		printf("%d %s\n", m[i].age, m[i].name);

	free(m);

	return 0;
}
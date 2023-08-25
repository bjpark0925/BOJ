#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct {
	int top;
	int* data;
}stack;

typedef struct {
	int tail;
	int* data;
}queue;

void stackInit(stack* s, int size)
{
	s->top = -1;
	s->data = (int*)malloc(sizeof(int) * size);
}

void queueInit(queue* a, int size)
{
	a->tail = -1;
	a->data = (int*)malloc(sizeof(int) * size);
}

void spush(stack* s, int value)
{
	s->top++;
	s->data[s->top] = value;
}

void qpush(queue* a, int value)
{
	a->tail++;
	a->data[a->tail] = value;
}

void pop(stack* s)
{
	s->data[s->top] = 0;
	s->top--;
}

int main() {

	int n;
	int flag = 0;
	int cnt = 1;

	scanf("%d", &n);

	stack s;
	stackInit(&s, n);

	queue a;
	queueInit(&a, 2 * n + 1);

	for (int i = 0; i < n; i++) {
		int num;
		scanf("%d", &num);

		while (cnt <= num) {
			spush(&s, cnt);
			qpush(&a, 1);
			cnt++;
		}

		if (s.data[s.top] == num) {
			pop(&s);
			qpush(&a, -1);
		}

		else {
			flag = 1;
			break;
		}
	}

	if (flag == 0) {
		for (int i = 0; i <= a.tail; i++) {
			if (a.data[i] == 1)
				printf("+\n");
			else if (a.data[i] == -1)
				printf("-\n");
		}
	}

	else
		printf("NO\n");

	return 0;
}
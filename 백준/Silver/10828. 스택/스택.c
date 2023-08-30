#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>//malloc

typedef struct {
	int data[10000];
	int top;
}Stack;

StackInit(Stack* s)
{
	s->top = -1;
}

int Empty(Stack* s)
{
	if (s->top == -1)
		return 1;
	else
		return 0;
}

void Push(Stack* s, int num)
{
	s->top++;
	s->data[s->top] = num;
}

void Pop(Stack* s)
{
	if (Empty(s))
		printf("%d\n", -1);
	else {
		printf("%d\n", s->data[s->top]);
		s->top--;
	}
}

int Size(Stack* s)
{
	return s->top + 1;
}

void Top(Stack* s)
{
	if (Empty(s))
		printf("%d\n", -1);
	else
		printf("%d\n", s->data[s->top]);
}

int main() {
	int n;
	scanf("%d", &n);
	Stack s;
	StackInit(&s);

	for (int i = 0; i < n; i++) {
		char order[6];
		scanf("%s", order);
		if (strcmp(order, "push") == 0) {
			int num;
			scanf("%d", &num);
			Push(&s, num);
		}
		else if (strcmp(order, "pop") == 0) {
			Pop(&s);
		}
		else if (strcmp(order, "size") == 0) {
			printf("%d\n", Size(&s));
		}
		else if (strcmp(order, "empty") == 0) {
			printf("%d\n", Empty(&s));
		}
		else if (strcmp(order, "top") == 0) {
			Top(&s);
		}
	}

	return 0;
}
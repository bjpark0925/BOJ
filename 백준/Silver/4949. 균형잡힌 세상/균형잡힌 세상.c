#pragma warning(disable: 4996)
#include<stdio.h>
#include<stdlib.h>//malloc
#include<string.h>//strlen
#define MAX 100

typedef struct {
	char* bracket[MAX + 1];
	int top;
}Stack;

void StackInit(Stack* s)
{
	s->top = -1;
}

void Push(Stack* s, char b)
{
	s->top++;
	s->bracket[s->top] = b;
}

int Pop(Stack* s, char b)
{
	if (b == ')') {
		if (s->bracket[s->top] == '(') {
			s->top--;
			return 1;
		}
		else
			return -1;
	}

	else if (b == ']') {
		if (s->bracket[s->top] == '[') {
			s->top--;
			return 1;
		}
		else
			return -1;
	}
}

int main() {
	while (1) {
		char* arr = (char*)malloc(sizeof(char) * (MAX + 1));
		scanf("%[^\n]s", arr);
		getchar();
		if (strlen(arr) == 1 && arr[0] == '.')
			break;

		Stack s;
		StackInit(&s);
		int flag = 1;
		for (int i = 0; i < strlen(arr); i++) {
			if (arr[i] == '(' || arr[i] == '[')
				Push(&s, arr[i]);
			if (arr[i] == ')' || arr[i] == ']')
				flag = Pop(&s, arr[i]);

			if (flag == -1) {
				printf("no\n");
				break;
			}
		}

		if (flag == -1)
			continue;
		if (s.top != -1) {
			printf("no\n");
			continue;
		}
		printf("yes\n");
	}

	return 0;
}
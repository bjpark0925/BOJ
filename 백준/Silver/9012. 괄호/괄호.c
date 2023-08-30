#pragma warning(disable: 4996)
#include<stdio.h>
#include<stdlib.h>//malloc
#include<string.h>//strlen
#define MAX 51

typedef struct {
	int top;
}Stack;

void StackInit(Stack* s)
{
	s->top = -1;
}

void Push(Stack* s)
{
	s->top++;
}

int Pop(Stack* s)
{
	if (s->top == -1)
		return -1;
	s->top--;
	return 1;
}

int main() {

	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		int flag = 1;
		char tmp[MAX];
		scanf("%s", tmp);
		
		Stack s;
		StackInit(&s);

		for (int j = 0; j < strlen(tmp); j++) {
			if (tmp[j] == '(')
				Push(&s);
			else if (tmp[j] == ')')
				flag = Pop(&s);

			if (flag == -1)
				break;
		}

		if (s.top == -1 && flag == 1)
			printf("YES\n");
		else
			printf("NO\n");
	}



	return 0;
}
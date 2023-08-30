#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>//malloc
#include<string.h>

typedef struct {
	int data;
	struct Node* pre;
	struct Node* next;
}Node;

typedef struct {
	int size;
	Node* front;
	Node* rear;
}Deque;

DequeInit(Deque* d)
{
	d->size = 0;
	d->front = d->rear = NULL;
}

int Empty(Deque* d)
{
	return d->size == 0;
}

void Push_front(Deque* d, int num)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = num;
	newNode->pre = NULL;
	newNode->next = NULL;
	if (Empty(d)) {
		d->front = d->rear = newNode;
	}
	else {
		newNode->next = d->front;
		d->front->pre = newNode;
		d->front = newNode;
	}
	d->size++;
}

void Push_back(Deque* d, int num)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = num;
	newNode->next = NULL;
	newNode->pre = NULL;
	if (Empty(d)) {
		d->front = d->rear = newNode;
	}
	else {
		newNode->pre = d->rear;
		d->rear->next = newNode;
		d->rear = newNode;
	}
	d->size++;
}

void Pop_front(Deque* d)
{
	if (Empty(d))
		printf("%d\n", -1);
	else {
		printf("%d\n", d->front->data);
		if (Size(d) == 1)
			free(d->front);
		else {
			d->front = d->front->next;
			free(d->front->pre);
		}
		d->size--;
	}
}

void Pop_back(Deque* d)
{
	if (Empty(d))
		printf("%d\n", -1);
	else {
		printf("%d\n", d->rear->data);
		if (Size(d) == 1)
			free(d->rear);
		else {
			d->rear = d->rear->pre;
			free(d->rear->next);
		}
		d->size--;
	}
}

int Size(Deque* d)
{
	return d->size;
}

void Front(Deque* d)
{
	if (Empty(d))
		printf("%d\n", -1);
	else
		printf("%d\n", d->front->data);
}

void Back(Deque* d)
{
	if (Empty(d))
		printf("%d\n", -1);
	else
		printf("%d\n", d->rear->data);
}

int main() {
	int n;
	scanf("%d", &n);
	Deque d;
	DequeInit(&d);

	for (int i = 0; i < n; i++) {
		char order[11];
		scanf("%s", order);
		if (strcmp(order, "push_front") == 0) {
			int num;
			scanf("%d", &num);
			Push_front(&d, num);
		}
		else if (strcmp(order, "push_back") == 0) {
			int num;
			scanf("%d", &num);
			Push_back(&d, num);
		}
		else if (strcmp(order, "pop_front") == 0) {
			Pop_front(&d);
		}
		else if (strcmp(order, "pop_back") == 0) {
			Pop_back(&d);
		}
		else if (strcmp(order, "size") == 0) {
			printf("%d\n", Size(&d));
		}
		else if (strcmp(order, "empty") == 0) {
			printf("%d\n", Empty(&d));
		}
		else if (strcmp(order, "front") == 0) {
			Front(&d);
		}
		else if (strcmp(order, "back") == 0) {
			Back(&d);
		}
	}

	return 0;
}
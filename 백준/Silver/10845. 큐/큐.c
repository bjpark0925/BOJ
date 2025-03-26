#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>//malloc

typedef struct {
	int data[10000];
	int front;
	int rear;
	int size;
}Queue;

QueueInit(Queue* q)
{
	q->front = q->rear = -1;
	q->size = 0;
}

int Empty(Queue* q)
{
	if (q->size == 0)
		return 1;
	else
		return 0;
}

void Push(Queue* q, int num)
{
	q->rear++;
	q->data[q->rear] = num;
	q->size++;
}

void Pop(Queue* q)
{
	if (Empty(q))
		printf("%d\n", -1);
	else {
		printf("%d\n", q->data[++q->front]);
		q->size--;
	}
}

int Size(Queue* q)
{
	return q->size;
}

void Front(Queue* q)
{
	if (Empty(q))
		printf("%d\n", -1);
	else {
		int temp = q->front;
		printf("%d\n", q->data[temp + 1]);
	}
}

void Back(Queue* q)
{
	if (Empty(q))
		printf("%d\n", -1);
	else
		printf("%d\n", q->data[q->rear]);
}

int main() {
	int n;
	scanf("%d", &n);
	Queue q;
	QueueInit(&q);

	for (int i = 0; i < n; i++) {
		char order[6];
		scanf("%s", order);
		if (strcmp(order, "push") == 0) {
			int num;
			scanf("%d", &num);
			Push(&q, num);
		}
		else if (strcmp(order, "pop") == 0) {
			Pop(&q);
		}
		else if (strcmp(order, "size") == 0) {
			printf("%d\n", Size(&q));
		}
		else if (strcmp(order, "empty") == 0) {
			printf("%d\n", Empty(&q));
		}
		else if (strcmp(order, "front") == 0) {
			Front(&q);
		}
		else if (strcmp(order, "back") == 0) {
			Back(&q);
		}
	}

	return 0;
}
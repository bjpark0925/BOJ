#pragma warning(disable: 4996)
#include<stdio.h>
#include<stdlib.h>//malloc
#include<string.h>//strlen
#include<stdbool.h>//true, false

typedef struct {
	int data;
	struct Node* next;
}Node;

typedef struct {
	Node* front;
	Node* rear;

	int cnt;
}Queue;

void QueueInit(Queue* queue)
{
	queue->front = queue->rear = NULL;
	queue->cnt = 0;
}

int isEmpty(Queue* queue)
{
	//true면 empty한 상태
	return queue->cnt == 0;
}

void Enqueue(Queue* queue, int num)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = num;
	newNode->next = NULL;

	if (isEmpty(queue)) {
		queue->front = newNode;
	}
	else {
		queue->rear->next = newNode;
	}

	queue->rear = newNode;
	(queue->cnt)++;
}

void Dequeue(Queue* queue)
{
	if (isEmpty(queue))
		return;

	Node* temp = queue->front;
	queue->front = queue->front->next;
	free(temp);
	(queue->cnt)--;
}

int main() {

	int n;
	scanf("%d", &n);

	Queue queue;
	QueueInit(&queue);

	for (int i = 1; i <= n; i++) {
		Enqueue(&queue, i);
	}

	while (queue.cnt!=1) {
		Dequeue(&queue);
		Enqueue(&queue, queue.front->data);
		Dequeue(&queue);
	}

	printf("%d\n", queue.front->data);

	return 0;
}

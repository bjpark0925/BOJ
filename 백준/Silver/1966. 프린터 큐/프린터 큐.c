#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>
typedef struct {
	int front;
	int rear;
	int* data;
}queue;

void queueInit(queue* q, int size)
{
	q->front = 0;
	q->rear = -1;
	q->data = (int*)malloc(sizeof(int) * size * size);
}

void push(queue* q, int value)
{
	q->rear++;
	q->data[q->rear] = value;
}

void pop(queue* q)
{
	q->data[q->front] = 0;
	q->front++;
}

void rearrange(queue* q)
{
	push(q, q->data[q->front]);
	pop(q);
}


int main() {
	int s;
	scanf("%d", &s);
	int* answer = (int*)malloc(sizeof(int) * s);
	int a = 0;

	while (s > 0) {
		int n, m, tmp;
		int cnt = 0, flag = 0;
		scanf("%d %d", &n, &m);

		int target = m;
		
		queue q;
		queueInit(&q, n);

		for (int i = 0; i < n; i++) {
			scanf("%d", &tmp);
			push(&q, tmp);
		}

		while (q.front<=q.rear) {
			//max값 찾기
			int max = q.data[q.front];
			for (int i = q.front; i <= q.rear; i++) {
				if (max < q.data[i])
					max = q.data[i];
			}

			int mcnt = 0;
			//중복 max 개수 구하기
			for (int i = q.front; i <= q.rear; i++) {
				if (max == q.data[i])
					mcnt++;
			}

			//max 출력하기 한 사이클
			for (int i = q.front; i <= q.rear; i++) {
				if (mcnt == 0)
					break;

				if (i == target) {
					if (q.data[i] == max) {
						cnt++;
						flag = 1;
						break;
					}
					else {
						target = q.rear + 1;
						rearrange(&q);
					}
				}

				else {
					if (q.data[i] == max) {
						pop(&q);
						cnt++;
						mcnt--;
					}
					else
						rearrange(&q);
				}
			}

			if (flag == 1)
				break;
		}

		answer[a] = cnt;
		a++;

		s--;
	}

	for (int i = 0; i < a; i++)
		printf("%d\n", answer[i]);

	return 0;
}
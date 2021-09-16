#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct Node {
	int data;
} node;

typedef struct Priority_queue {
	node heap[100];
	int size;
} priority_queue;

void push(priority_queue *pq, int value)
{
	int i = 0;
	pq->size++;
	i = pq->size;
	pq->heap[i].data=value;
	while (i > 1)
	{
		if (pq->heap[i / 2].data < pq->heap[i].data) // 새로 들어온 원소와 자신의 부모 노드와의 크기 비교, 스왑을 하기 위해서!
		{
			pq->heap[i].data = pq->heap[i / 2].data ^ pq->heap[i].data; // ^ and 연산을 통한 메모리 낭비 없는 스왑?
			pq->heap[i / 2].data = pq->heap[i].data ^ pq->heap[i / 2].data;
			pq->heap[i].data = pq->heap[i].data ^ pq->heap[i / 2].data;
			i /= 2;
		}
		else 
		{
			break;
		}
	}
}

int pop_top(priority_queue* pq)
{
	int i = 1;
	int j = 0;
	pq->heap[i].data = pq->heap[pq->size--].data;

	while (i <= pq->size) 
	{
		j = 2 * i;
		if (j > pq->size) 
		{
			break;

		}
		if (pq->heap[i].data >= pq->heap[j].data && pq->heap[i].data >= pq->heap[j + 1].data) 
		{
			break;
		}
		if (pq->heap[j].data > pq->heap[j + 1].data) {

			j = j + 1;

		}
		pq->heap[i].data = pq->heap[j].data ^ pq->heap[i].data; // ^ and 연산을 통한 메모리 낭비 없는 스왑?
		pq->heap[j].data = pq->heap[i].data ^ pq->heap[j].data;
		pq->heap[i].data = pq->heap[i].data ^ pq->heap[j].data;
		i = j;
	}
}

int pop(priority_queue *pq)
{
	int i = 1;
	int k = 1;
	int mx = 0;

	while (i <= pq->size)
	{
		for (int j = 1; j <= pow(2, k - 1); j++)
		{
			if (i > pq->size)
			{
				break;
			}
			return pq->heap[i].data;
		}
		k++;	
	}
}

int main()
{
	int n;
	int ans = 0;
	priority_queue pq;
	pq.size = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int input;
		scanf("%d", &input);
		push(&pq, input);
	}
	for (int i = 0; i < n; i++)
	{
		int top = pop(&pq);
		ans = max(ans, top*(i+1));
		pop_top(&pq);
	}
	printf("%d", ans);
}
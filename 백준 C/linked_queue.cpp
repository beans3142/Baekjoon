#include <stdio.h>

int n, m;

typedef struct queue
{
	int data[101];
	int front = -1;
	int back = -1;
} QUEUE;

void PUSH(QUEUE* queue, int data)
{
	(*queue).data[(++(*queue).back)%n] = data;
}

int POP(QUEUE* queue)
{
	return (*queue).data[(++(*queue).front)%n];
}

int SIZE(QUEUE* queue)
{
	return (*queue).back - (*queue).front;
}

int FRONT(QUEUE* queue)
{
	return (*queue).data[((*queue).front + 1)%n];
}

int BACK(QUEUE* queue)
{
	return (*queue).data[((*queue).back)%n];
}

int main()
{
	int typ, data;
	QUEUE queue;
	scanf("%d %d", &n, &m);

	for (int i = 0; i < m; i++)
	{
		scanf("%d", &typ);
		if (typ == 1)
		{
			scanf("%d", &data);
			if (SIZE(&queue) < n)
			{
				PUSH(&queue, data);
			}
			else
			{
				printf("Overflow\n");
			}
		}
		else if (typ == 2)
		{
			if (SIZE(&queue) > 0)
			{
				POP(&queue);
			}
			else
			{
				printf("Underflow\n");
			}
		}
		else
		{
			if (SIZE(&queue) > 0)
			{
				printf("%d\n", FRONT(&queue));
			}
			else
			{
				printf("NULL\n");
			}
		}
	}
}
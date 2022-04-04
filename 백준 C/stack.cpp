#include <stdio.h>
#include <stdlib.h>

typedef struct stack
{
	int data[1001];
	int top = -1;
} STACK;

void push(STACK *stack, int data)
{
	(*stack).top += 1;
	(*stack).data[(*stack).top] = data;
}

int pop(STACK *stack)
{
	return (*stack).data[(*stack).top--];
}

int peak(STACK *stack)
{
	return (*stack).data[(*stack).top];
}

int getsize(STACK *stack)
{
	return (*stack).top + 1;
}

int main_stack()
{
	int n,m;
	int typ,data;
	scanf("%d %d", &n, &m);
	STACK stack;
	for (int i = 0; i < m; i++)
	{
		scanf("%d", &typ);
		if (typ == 1)
		{
			scanf("%d", &data);
			if (getsize(&stack)<n)
			{
				push(&stack, data);
			}
			else
			{
				printf("Overflow\n");
			}
		}
		else if(typ==2)
		{
			if (getsize(&stack) != 0)
			{
				data = pop(&stack);
			}
			else
			{
				printf("Underflow\n");
			}
		}
		else
		{
			if (getsize(&stack) != 0)
			{
				data = peak(&stack);
				printf("%d\n", data);
			}
			else
			{
				printf("NULL\n");
			}
		}
	}
	return 0;
}
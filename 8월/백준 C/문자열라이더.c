#include <stdio.h>

int len;
char s[1000];

void reverse()
{
	int idx = 0;
	char reversed_s[1000];
	for (int i = len-1; i >= 0; i--)
	{
		reversed_s[idx++] = s[i];
	}
	for (int i = 0; i < len; i++)
	{
		s[i] = reversed_s[i];
	}
}

void say()
{
	for (int i = 0; i < len; i++)
	{
		printf("%c", s[i]);
	}
	printf("\n");
}

int main()
{
	int t;
	scanf("%s", s);

	for (len = 0; s[len] != '\0'; len++);

	scanf("%d", &t);
	while (t--)
	{
		int thief;
		scanf("%d", &thief);
		if (thief == 3)
		{
			len--;
			if (len == 0)
			{
				break;
			}
			say();
		}
		else if (thief == 2)
		{
			reverse();
			say();
		}
		else
		{
			printf("%d\n", len);
		}
	}
	if (len > 0)
	{
		printf("happy!");
	}
	else
	{
		printf("Die");
	}
	return 0;
}
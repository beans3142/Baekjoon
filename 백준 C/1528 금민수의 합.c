#include <stdio.h>

int count_4_and_7[2] = { 0,0 };
int mn = 10000000;
int able = 0;
int work = 1;

int dfs(int x, int div_four, int div_seven)
{
	if (work == 1)
	{
		if (x < 4)
		{
			return;
		}
		if (x == 4)
		{
			if (div_four + div_seven < mn)
			{
				able = 1;
				mn = div_four + div_seven;
				count_4_and_7[0] = div_four + 1;
				count_4_and_7[1] = div_seven;
			}
			work = 0;
			return 0;
		}
		if (x == 7)
		{
			if (div_four + div_seven < mn)
			{
				able = 1;
				mn = div_four + div_seven;
				count_4_and_7[0] = div_four;
				count_4_and_7[1] = div_seven + 1;
			}
			work = 0;
			return 0;
		}
		if (x % 7 == 0)
		{
			dfs(x / 7, div_four, div_seven + x / 7);
		}
		else if (x % 4 == 0)
		{
			dfs(x / 4, div_four + x / 4, div_seven);
		}

		dfs(x - 7, div_four, div_seven + 1);
		dfs(x - 4, div_four + 1, div_seven);
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	dfs(n, 0, 0);
	for (int i = 0; i < count_4_and_7[0]; i++)
	{
		printf("4 ");
	}
	for (int i = 0; i < count_4_and_7[0]; i++)
	{
		printf("7 ");
	}
	if (able == 0)
	{
		printf("-1");
	}
}
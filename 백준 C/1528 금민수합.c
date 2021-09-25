#include <stdio.h>

int n;
int able = 1;

void dfs(int val, int fc, int sc)
{
	if (able)
	{
		if (val < n)
		{
			dfs(val + 7, fc, sc + 1);
			dfs(val + 4, fc + 1, sc);
		}
		if (val == n)
		{
			for (int i = 0; i < fc; i++) printf("4 ");
			for (int i = 0; i < sc; i++) printf("7 ");
			able = 0;
		}
	}
	return 0;
}

int main2()
{
	scanf("%d", &n);
	dfs(0, 0, 0);
	if (able) printf("-1");
	return 0;
}
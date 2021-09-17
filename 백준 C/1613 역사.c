#include <stdio.h>

int history_mn[401][401];

int max(int num1, int num2)
{
	return num1 < num2 ? num2 : num1;
}

int main()
{
	int n, k;
	scanf("%d %d", &n, &k);
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			history_mn[i][j] = 0;
		}
	}
	for (int i = 0; i < k; i++)
	{
		int a, b;
		scanf("%d %d", &a, &b);
		history_mn[a][b] = 1;
	}
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			for (int k = 1; k <= n; k++)
			{
				if (history_mn[j][i] == 1&& history_mn[i][k]==1)
				{
					history_mn[j][k] = 1;
				}
			}
		}
	}

	/*printf("\n\n");
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			printf("%7d ", history_mn[i][j]);
		}
		printf("\n");
	}
	printf("\n\n");*/
	
	int s;
	scanf("%d", &s);
	for (int i = 0; i < s; i++)
	{
		int a, b;
		scanf("%d %d", &a, &b);
		if (history_mn[a][b] == 1)
		{
			printf("-1");
		}
		else if (history_mn[b][a]==1)
		{
			printf("1");
		}
		else
		{
			printf("0");
		}
		printf("\n");
	}
}
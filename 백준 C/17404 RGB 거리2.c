#include <stdio.h>

int dp[1001][3];
int rgb[1001][3];

int min(int num1, int num2)
{
	return num1 > num2 ? num2 : num1;
}

int main()
{
	int n;
	int ans = 1<<20;
	int mx = ans;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			int num;
			scanf("%d", &num);
			rgb[i][j]=num;
		}
	}
	for (int j = 0; j < 3; j++)
	{
		for (int i = 0; i < 3; i++)
		{
			if (i == j)
			{
				dp[1][i] = rgb[1][i];
			}
			else
			{
				dp[1][i] = mx;
			}
		}

		for (int i = 2; i <= n; i++)
		{
			dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0];
			dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1];
			dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2];
		}
		for (int i = 0; i <= 2; i++)
		{
			if (i == j) continue;
			ans = min(ans, dp[n][i]);
		}

	}
	printf("%d", ans);
}
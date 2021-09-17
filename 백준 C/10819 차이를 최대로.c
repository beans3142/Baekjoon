#include <stdio.h>
#include <math.h>

int vi[8] = {0,};
int arr[8] = { 0, };
int n;
int ans = 0;

int dfs(int x[],int depth)
{
	if (depth==n)
	{
		int sum = 0;
		for (int i = 1; i < n; i++)
		{
			sum += abs(x[i-1] - x[i]);
		}
		/*for (int i = 0; i < n; i++)
		{
			printf("%d ", x[i]);
		}
		printf("\n");*/
		ans = sum>ans ? sum : ans;
	}
	else {
		for (int i = 0; i < n; i++)
		{
			if (vi[i] == 0)
			{
				vi[i] = 1;
				x[depth] = arr[i];
				dfs(x, depth + 1);
				vi[i] = 0;
			}
		}
	}
}

int main()
{

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int num;
		scanf("%d", &num);
		arr[i] = num;
	}
	int bt[8] = { 0, };
	dfs(bt, 0);
	printf("%d", ans);

	return 0;
}
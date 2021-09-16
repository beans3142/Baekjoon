#include <stdio.h>

int baechoo[51][51] = { 0, };
int vi[51][51] = { 0, };
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };

void dfs(int x, int y, int m, int n)
{
	for (int i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (-1 < nx && nx < m && -1 < ny && ny < n)
		{
			if (vi[ny][nx] == 0 && baechoo[ny][nx] == 1)
			{
				vi[ny][nx] = 1;
				dfs(nx, ny, m, n);
			}
		}
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int j = 0; j < t; j++)
	{
		int n, m, k;
		int cnt = 0;
		scanf("%d %d %d", &m,&n,&k);
		for (int i = 0; i < k; i++)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			baechoo[b][a] = 1;
		}
		for (int i = 0; i < n; i++)
		{
			for (int l = 0; l < m; l++)
			{
				if (vi[i][l] == 0 && baechoo[i][l]==1)
				{
					vi[i][l] = 1;
					cnt++;
					dfs(l, i, m, n);
				}
			}
		}
		for (int i = 0; i < n; i++)
		{
			for (int l = 0; l < m; l++)
			{
				vi[i][l] = 0;
				baechoo[i][l] = 0;
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}
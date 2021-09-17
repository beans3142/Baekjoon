#include <stdio.h>

int dx[8] = { 0,0,-1,-1,-1,1,1,1 };
int dy[8] = { 1,-1,1,0,-1,1,0,-1 };
int w, h;
arr[50][50] = { 0, };


int dfs(int x, int y)
{
	for (int i = 0; i < 8; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (-1 < nx && nx < w && -1 < ny && ny < h)
		{
			if (arr[ny][nx] == 1)
			{
				arr[ny][nx] = 0;
				dfs(nx,ny);
			}
		}
	}
}

int main()
{
	while (1)
	{
		scanf("%d %d", &w, &h);
		if (w==0 && h==0)
		{
			break;
		}
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				scanf("%d", &arr[i][j]);  
			}
		}
		int cnt = 0;
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (arr[i][j] == 1)
				{
					arr[i][j] = 0;
					dfs(j, i);
					cnt++;
				}
			}
		}
		printf("%d\n",cnt);
	}
}
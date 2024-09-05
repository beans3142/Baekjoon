#include <iostream>

using namespace std;

int n,vi[500][500] = {0,};
int arr[500][500];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

int dfs(int x, int y)
{
	int cnt = 1;
	for (int i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (-1 < nx && nx < n && -1 < ny && ny < n)
		{
			if (arr[ny][nx] < arr[y][x])
			{
				if (vi[ny][nx] == 0)
				{
					vi[ny][nx] = dfs(nx, ny);
				}
				cnt = max(cnt, vi[ny][nx] + 1);
			}
		}
	}
	return cnt;
}

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);
	
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> arr[i][j];
		}
	}
	int ans = 1;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (vi[i][j] == 0)
			{
				ans = max(ans, dfs(j, i));
			}
		}
	}
	cout << ans;
}
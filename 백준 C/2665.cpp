#include <iostream>
#include <deque>
#include <cstring>

using namespace std;

int main()
{
	int n;
	int dx[4] = { 1,-1,0,0 };
	int dy[4] = { 0,0,1,-1 };

	deque<pair<int,int>> dq;

	string arr[50];
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}

	int vi[50][50];
	memset(vi, -1, sizeof(vi));
	vi[0][0] = 0;
	dq.push_front({ 0,0 });


	while (!dq.empty())
	{
		int x = dq.front().first;
		int y = dq.front().second;
		dq.pop_front();
		for (int i = 0; i < 4; i++)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (-1 < nx && nx < n && -1 < ny && ny < n)
			{
				if (vi[ny][nx] == -1)
				{
					if (arr[ny][nx] == '1')
					{
						vi[ny][nx] = vi[y][x];
						dq.push_front({ nx,ny });
					}
					else
					{
						vi[ny][nx] = vi[y][x] + 1;
						dq.push_back({ nx,ny });
					}
				}
			}
		}
	}
	cout << vi[n - 1][n - 1];
}
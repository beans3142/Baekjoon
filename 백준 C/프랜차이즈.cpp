#include <iostream>
#include <queue>
#include <algorithm>
#include <stack>

using namespace std;

int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };

queue< pair<int, int>> dots[10] = {};
int arr[1001][1001];
int vi[10][1001][1001];
int n, m;

void bfs(int idx);

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);
	string s;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		for (int j = 0; j < m; j++)
		{
			arr[i][j] = s[j]-'0';
			dots[arr[i][j]].push(make_pair(j,i));
		}
	}

	for (int idx = 0; idx < 10; idx++)
	{
		bfs(idx);
	}

	int q;
	cin >> q;
	int y, x, cnt;
	while (q--)
	{
		cin >> y >> x >> cnt;
		cin >> s;
		for (int i = 0; i < cnt; i++)
		{
			cout<< vi[s[i]-'0'][y-1][x-1]-1 << " ";
		}
		cout << "\n";
	}
	
}

void bfs(int idx)
{
	queue<pair<int, int>> q;
	int le = dots[idx].size();
	int dist = 1;
	int x, y, nx, ny;

	for (int i = 0; i < le; i++)
	{
		x = dots[idx].front().first;
		y = dots[idx].front().second;
		vi[idx][y][x] = dist;
		dots[idx].push(make_pair(x, y));
		dots[idx].pop();
	}

	while (!dots[idx].empty())
	{
		dist += 1;
		le = dots[idx].size();
		for (int i = 0; i < le; i++)
		{
			x = dots[idx].front().first;
			y = dots[idx].front().second;
			dots[idx].pop();
			for (int j = 0; j < 4; j++)
			{
				nx = x + dx[j];
				ny = y + dy[j];
				if (-1 < nx && nx < m && -1 < ny && ny < n)
				{
					if (vi[idx][ny][nx] == 0)
					{
						vi[idx][ny][nx] = dist;
						dots[idx].push(make_pair(nx,ny));
					}
				}
			}
		}
	}
}
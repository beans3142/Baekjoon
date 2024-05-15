#include <iostream>
#include <queue>
#include <tuple>
#include <vector>
#include <algorithm>

#define MAX 1001
#define INF 2000000001

using namespace std;

vector<tuple<int, int, int>> graph[MAX];
int vi[MAX][MAX];

int dijkstra(int N, int L)
{
	int ch, co, now;
	for (int i = 0; i < MAX; i++)
	{
		for (int j = 0; j < MAX; j++)
		{
			vi[i][j] = INF;
		}
	}
	vi[0][1] = 0;
	priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;

	pq.push(make_tuple(0, 0, 1));
	while (!pq.empty())
	{
		ch = get<0>(pq.top()); co = get<1>(pq.top()); now = get<2>(pq.top());
		pq.pop();
		//cout << ch << " " << co << " " << now << endl;
		if (vi[ch][now] < co) continue;
		for (auto nxt : graph[now])
		{
			int nxch = ch + get<0>(nxt);
			int nxco = co + get<2>(nxt);
			int nx = get<1>(nxt);
			if ( nxch < MAX && nxco < vi[nxch][nx] && nxco <= L)
			{
				vi[nxch][nx] = nxco;
				pq.push(make_tuple(nxch, nxco, nx));
			}
		}
	}
	for (int i = 0; i <= N; i++) if (vi[i][N] != INF) return i; //cout << i << " " << vi[i][N] << endl;
	return -1;
}

int main()
{
	int N, M, L, A, B, C;
	cin >> N >> M >> L;
	for (int i = 0; i < M; i++)
	{
		cin >> A >> B >> C;
		graph[A].push_back(make_tuple(0, B, C));
		graph[B].push_back(make_tuple(1, A, C));
	}
	for (int i = 1; i <= N; i++)
	{
		sort(graph[i].begin(), graph[i].end());
	}
	cout << dijkstra(N, L);
}
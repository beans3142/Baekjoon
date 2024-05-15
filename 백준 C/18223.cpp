#include <iostream>
#include <queue>

#define MX 5001
#define INF 100000000

using namespace std;

vector<pair<int,int>> graph[MX];

pair<int,int> dijk(int s,int e1,int e2)
{
	int co,now,vi[MX];
	for (int i = 1; i < MX; i++) vi[i] = INF;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0,s });
	vi[s] = 0;

	while (!pq.empty())
	{
		co = pq.top().first; now = pq.top().second;
		pq.pop();

		if (co > vi[now]) continue;
		for (auto nxt : graph[now])
		{
			if(co+nxt.second<vi[nxt.first])
			{
				vi[nxt.first] = nxt.second + co;
				pq.push({vi[nxt.first],nxt.first});
			}
		}
	}
	return {vi[e1],vi[e2]};
}

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);

	int v, e, p, a, b, c;
	cin >> v >> e >> p;

	for (int i = 0; i < e; i++)
	{
		cin >> a >> b >> c;
		graph[a].push_back({ b,c });
		graph[b].push_back({ a,c });
	}
	int shrt = dijk(1, v, 0).first;
	pair<int,int> fromp = dijk(p, 1, v);
	if (shrt == fromp.first + fromp.second) cout << "SAVE HIM";
	else cout << "GOOD BYE";
}
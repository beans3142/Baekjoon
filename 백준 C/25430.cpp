#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

#define MAX 100001

using namespace std;

typedef long long ll;
vector<pair<int, int>> graph[MAX];
ll val[MAX];

ll dijk(int s, int e)
{
	ll cost, INF = 10000000000000000;
	int now, bef;
	priority_queue<pair<ll, pair<int, int>>, vector<pair<ll, pair<int, int>>>, greater<pair<ll, pair<int, int>>>> pq;
	for (int i = 1; i < MAX; i++) val[i] = INF;
	val[s] = 0;
	pq.push({ 0,{0,s} });
	while (!pq.empty())
	{
		cost = pq.top().first;
		now = pq.top().second.second; bef = pq.top().second.first;
		pq.pop();
		if (now == e) return cost;
		for (pair<int, int> nxt : graph[now])
		{
			if (bef < nxt.second)
			{
				val[nxt.first] = min(val[nxt.first], nxt.second + cost);
				pq.push({ nxt.second + cost,{nxt.second,nxt.first} });
			}
		}
	}
	return -1;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cout.tie(0);
	cin.tie(0);
	int n, m, a, b, c;
	int s, e;
	cin >> n >> m;
	for (int i = 0; i <	m; i++)
	{
		cin >> a >> b >> c;
		graph[a].push_back({ b,c });
		graph[b].push_back({ a,c });
	}
	cin >> s >> e;
	ll ans = dijk(s, e);
	if (ans != -1) cout << ans;
	else cout << "DIGESTA";
}
#include <iostream>
#include <queue>
#include <algorithm>

#define MAX 1001
#define INF 1000000001

using namespace std;

vector<pair<int, int>> graph[MAX];
vector<pair<int, int>> pp;
vector<pair<int, int>> qq;


int dijk(int N,vector<pair<int, int>> start, vector<pair<int, int>> end)
{
	int elen = end.size();
	int mx,ans = 0;
	for (auto s : start)
	{
		int now, cost, vi[MAX];
		for (int i = 1; i <= N; i++) vi[i] = INF;
		priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
		pq.push(make_pair(0, s.first));
		vi[s.first] = 0;


		while (!pq.empty())
		{
			cost = pq.top().first;
			now = pq.top().second;
			pq.pop();
			if (vi[now] < cost) continue;
			for (auto nextp : graph[now])
			{
				if (vi[nextp.first] > cost + nextp.second)
				{
					vi[nextp.first] = cost+nextp.second;
					pq.push(make_pair(vi[nextp.first], nextp.first));
				}
			}
		}
		mx = -INF;
		for (auto endp : end)
		{
			mx = max(endp.second + s.second - vi[endp.first], mx);
		}
		ans = max(ans, mx);
	}
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	int n, c,p,q;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			cin >> c;
			if (c != 0)
			{
				graph[i].push_back(make_pair(j, c));
			}
		}
	}
	int loc, exp;
	cin >> p >> q;
	for (int i = 0; i < p; i++)
	{
		cin >> loc >> exp;
		pp.push_back(make_pair(loc, exp));
	}
	for (int i = 0; i < q; i++)
	{
		cin >> loc >> exp;
		qq.push_back(make_pair(loc, exp));
	}
	if (pp.size() < qq.size())
	{
		cout << dijk(n, pp, qq);
	}
	else
	{
		cout << dijk(n, qq, pp);
	}

}
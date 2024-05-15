#include <iostream>
#include <vector>
#include <tuple>
#include <unordered_set>

using namespace std;

int par[3001];

int find(int x)
{
	if (x == par[x]) return x;
	par[x] = find(par[x]);
	return par[x];
}

void uni(int a,int b)
{
	a = find(a);
	b = find(b);
	if (a < b) par[b] = a;
	else par[a] = b;
}

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;
	while (t--)
	{
		int n,x,y,r,d1,d2,d3;
		vector<tuple<int,int,int>> v;

		cin >> n;

		for (int i = 0; i < n; i++) par[i] = i;

		for (int i = 0; i < n; i++)
		{
			cin >> x >> y >> r;
			v.push_back(make_tuple(x, y, r));
			for (int j = 0; j < i; j++)
			{
				d1 = (get<0>(v[i]) - get<0>(v[j])) * (get<0>(v[i]) - get<0>(v[j]));
				d2 = (get<1>(v[i]) - get<1>(v[j])) * (get<1>(v[i]) - get<1>(v[j]));
				d3 = (get<2>(v[i]) + get<2>(v[j])) * (get<2>(v[i]) + get<2>(v[j]));
				if (d1 + d2 <= d3)
				{
					uni(i, j);
				}
			}
		}
		unordered_set<int> uos;
		//for (int i = 0; i < n; i++) find(i);
		for (int i = 0; i < n; i++) uos.insert(find(i));
		cout << uos.size() << "\n";
	}
}
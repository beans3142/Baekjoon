#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int par[3001];

int find(int x)
{
	if (par[x] == x) return x;
	par[x] = find(par[x]);
	return par[x];
}

void uni(int a, int b)
{
	a = find(a);
	b = find(b);
	if (a < b) par[b] = a;
	else par[a] = b;
}

int main()
{

	int n, m, a, b, de=-1;
	cin >> n >> m;

	vector<pair<int, int>> con;
	vector<int> dearr;
	pair<int, int> pp;

	for (int i = 0; i < m; i++)
	{

		cin >> a >> b;
		con.push_back({ a,b });

	}
	for (int i = 1; i <= n; i++) par[i] = i;
	for (int t = 0; t < n; t++)
	{

		int le = con.size();
		vector<pair<int, int>> ncon;
		while (le--)
		{
			a=con.back().first;
			b = con.back().second;
			con.pop_back();
			pp = {a,b};
			if (a != de && b != de)
			{
				ncon.push_back(pp);
				uni(a, b);
			}
		}

		unordered_set<int> uos;
		for (int i = 1; i <= n; i++) if (par[i]!=-1) uos.insert(find(i));
		//for (int i = 1; i <= n; i++) cout << par[i] << " ";
		//cout << "\n";
		while (!ncon.empty())
		{
			con.push_back(ncon.back());
			ncon.pop_back();
		}
		//cout << uos.size() << " " << con.size() << "\n";
		if (uos.size() != 1) cout << "NO\n";
		else cout << "YES\n";

		cin >> de;
		par[de] = -1;
		for (int i = 1; i <= n; i++) if (par[i] != -1) par[i] = i;

	}
}
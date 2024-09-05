#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	while (t--)
	{
		int n,a,b,cnt=0;
		cin >> n;
		vector<pair<int, int>> vec;
		for (int i = 0; i < n; i++)
		{
			cin >> a >> b;
			vec.push_back({ a,b });
		}
		sort(vec.begin(), vec.end());
		int mx = 100001;
		for (int i = 0; i < n; i++)
		{
			cnt += mx > vec[i].second;
			mx = min(mx, vec[i].second);
		}
		cout << cnt << "\n";
	}
}
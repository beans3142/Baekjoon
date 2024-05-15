#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int check(int n, unordered_map<int, bool>* visited)
{
	if ((*visited)[n] == true) return 0;
	(*visited)[n] = true;
	while (n > 0)
	{
		if (!(n % 10 == 5 || n % 10 == 8)) return 0;
		n /= 10;
	}
	return 1;
}

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		unordered_map<int, bool> visited;
		unordered_map<int, bool>* p = &visited;
		int n,m,k, ans=0; 
		cin >> n;
		vector<int> v1(n);
		for (auto& i : v1) cin >> i;
		cin >> m;
		vector<int> v2(m);
		for (auto& i : v2) cin >> i;
		cin >> k;
		vector<int> v3(k);
		for (auto& i : v3) cin >> i;

		for (auto i : v1) for (auto j : v2) for (auto l: v3) ans+=check(i+j+l, p);
		cout << ans << "\n";
		
	}
}
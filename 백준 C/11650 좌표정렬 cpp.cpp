#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int n;
	cin >> n;
	priority_queue<pair<int,int>,vector<pair<int, int>>,greater<pair<int,int>>> pq;
	while (n--)
	{
		int x, y;
		cin >> x >> y;
		pq.push({ x, y });
	}
	while (!pq.empty())
	{
		cout << pq.top().first <<' ' << pq.top().second << '\n';
		pq.pop();
	}
}
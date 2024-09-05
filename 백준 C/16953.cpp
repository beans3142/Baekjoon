#include <iostream>
#include <deque>

using namespace std;

typedef long long ll;

int main()
{
	ll a, b;
	cin >> a >> b;
	int t = 0;

	deque<int> dq;
	dq.push_back(a);
	while (!dq.empty())
	{
		int len = dq.size();
		while (len--)
		{
			ll now = dq.front();
			if (now == b)
			{
				cout << t + 1;
				return 0;
			}
			dq.pop_front();
			if (now * 10 + 1 <= b) dq.push_back(now * 10 + 1);
			if (now * 2 <= b) dq.push_back(now * 2);
		}
		t++;
	}
	cout << -1;
}
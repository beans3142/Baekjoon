#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);

	long long int n, m, div, ans=0;
	cin >> n >> m;
	ans = m - n + 1;
	for (int i = 1; i < 100; i++)
	{
		div = pow(2, i);
		if (div > m) break;
		ans += ((m / div - (n - 1) / div) * (div / 2));
	}
	cout << ans;
}
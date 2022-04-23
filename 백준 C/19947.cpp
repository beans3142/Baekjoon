#include <iostream>
#include <math.h>
#include <algorithm>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);

	int h, y;
	cin >> h >> y;
	int dp[17] = {0,};
	dp[0] = h;

	for (int i = 0; i < y; i++)
	{
		dp[i + 1] = max(dp[i+1], (int)(dp[i]*1.05));
		dp[i + 3] = max(dp[i + 3], (int)(dp[i]*1.2));
		dp[i + 5] = max(dp[i + 5], (int)(dp[i]*1.35));
	}
	cout << *max_element(dp,dp+y+1);
}
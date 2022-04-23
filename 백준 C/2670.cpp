#include <iostream>
#include <math.h>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long ll;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);

	long double arr[10001];
	long double dp[10001];
	int n;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	dp[0] = arr[0];
	for (int i = 1; i < n; i++)
	{
		if (dp[i - 1] * arr[i] < 1)
		{
			dp[i] = arr[i];
		}
		else
		{
			dp[i] = arr[i] * dp[i - 1]>arr[i] ? arr[i] * dp[i - 1] : arr[i];
		}
	}
	cout.setf(ios::fixed);
	cout.precision(3);
	cout << *max_element(dp, dp + n);
}
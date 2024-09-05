#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);

	int n, k;
	cin >> n >> k;
	int arr[101];
	int dp[10001] = {1,};
	for (int i = 0; i < n; i++)
	{
		int a; cin >> a;
		arr[i] = a;
	}
	for (int i=0;i<n;i++)
	{
		for (int j = arr[i]; j <= k; j++)
		{
			dp[j] += dp[j-arr[i]];
		}
	}
	cout << dp[k];
}
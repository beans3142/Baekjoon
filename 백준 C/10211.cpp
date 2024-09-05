#include <iostream>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);

	int t, n, x;
	cin >> t;
	while (t--)
	{
		int n;
		int arr[1001] = {0,};
		cin >> n;
		cin >> arr[1];
		int ans = -100000000;
		for (int i = 2; i <= n; i++)
		{
			int num; cin >> num;
			arr[i] = arr[i - 1] + num;
		}
		for (int i = 0; i <= n; i++)
		{
			for (int j = i + 1; j <= n; j++)
			{
				ans = max(ans, arr[j] - arr[i]);
			}
		}
		cout << ans << "\n";
	}
}
#include <iostream>

using namespace std;

int arr[100001];

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);
	int n, m;
	cin >> n >> m;

	for (int i = 0; i < m; i++) cin >> arr[i];

	int s = 0;
	int idx = 0;
	int ans = max(n-arr[m-1],arr[0]);
	while (idx<m)
	{
		if (s + ans < arr[idx] - ans)
		{
			ans = (arr[idx] - s + 1) / 2;
		}
		s = arr[idx++];
	}
	cout << ans;
}
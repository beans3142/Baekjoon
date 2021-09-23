#include <iostream>
#include <cstring>
using namespace std;

const int N = 1000002, M = 102;
int n, m, W[M], V[M], bag[M], dp[M][N];
int max_val = 0;

int main() {
	cin.tie(0); cout.tie(0);

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> W[i] >> V[i];
	}
	for (int i = 0; i < m; i++) {
		cin >> bag[i];
	}

	for (int i = 0; i <= n; i++) {
		for (int j = 0; j < N; j++) {
			if (i == 0 || j == 0) dp[i][j] = 0;
			else if (W[i - 1] <= j) dp[i][j] = max(V[i - 1] + dp[i - 1][j - W[i - 1]], dp[i - 1][j]);
			else dp[i][j] = dp[i - 1][j];
		}
	}

	int ans = 0;
	int val1 = 0, val2 = 0;

	for (int i = 0; i < m; i++) {
		int x = dp[n][bag[i]];
		int a = x / bag[i];
		int b = x % bag[i];

		if (a > val1 || (a == val1 && b > val2)) {
			ans = i + 1;
			val1 = a; val2 = b;
		}
	}

	cout << ans << endl;

	return 0;
}
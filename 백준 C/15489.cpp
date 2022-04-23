#include <iostream>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);

	int pascal[33][33] = {0,};
	pascal[0][1] = 1;
	for (int i = 0; i < 30; i++)
	{
		for (int j = 1; j <= i+1; j++)
		{
			pascal[i + 1][j] += pascal[i][j];
			pascal[i + 1][j + 1] += pascal[i][j];
		}
	}

	for (int i = 0; i < 31; i++)
	{
		for (int j = 1; j <= i + 1; j++)
		{
			pascal[i][j] = pascal[i][j - 1] + pascal[i][j];
		}
	}

	int r, c, w;
	cin >> r >> c >> w;
	int ans = 0;

	for (int i = 0; i < w; i++)
	{
		ans += pascal[r - 1 + i][c+i] - pascal[r - 1 + i][c - 1];
	}

	cout << ans;
}
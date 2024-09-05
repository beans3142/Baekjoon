#include <iostream>

using namespace std;

int garo[5] = { 0,0,0,0,0 };
int sero[5] = { 0,0,0,0,0 };
int num[25];
int n, mask = 31;

bool check(int n)
{
	garo[n / 5]=garo[n/5]|(1<<(n % 5));
	sero[n % 5]=sero[n%5]|(1<<(n / 5));
	int cnt=0;
	for (int i = 0; i < 5; i++)
	{
		if (!(garo[i] ^ mask)) cnt += 1;
		if (!(sero[i] ^ mask)) cnt += 1;
	}
	if ((garo[0] & 1) && (garo[1] & 2) && (garo[2] & 4) && (garo[3] & 8) && (garo[4] & 16)) cnt += 1;
	if ((garo[4] & 1) && (garo[3] & 2) && (garo[2] & 4) && (garo[1] & 8) && (garo[0] & 16)) cnt += 1;

	return cnt >= 3;
}

int main()
{
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			cin >> n;
			num[n-1] = i * 5 + j;
		}
	}
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			cin >> n;
			if (check(num[n-1]))
			{
				cout << i * 5 + j + 1;
				return 0;
			}
		}
	}
}
#include <iostream>

using namespace std;

int n,hp;
int matrix[5][2];
int cool[5] = {0,};
int ans = 100000000;

int bt(int time, int damage)
{
	if (damage >= hp)
	{
		ans = min(ans, time);
		return 0;
	}
	bool use=false;
	for (int i = 0; i < n; i++)
	{
		if (cool[i] <= time)
		{
			use = true;
			int tmp = cool[i];
			cool[i] = time + matrix[i][0];
			bt(time + 1, damage + matrix[i][1]);
			cool[i] = tmp;
		}
	}
	if (!use) bt(time + 1, damage);
	return 0;
}

int main()
{
	cin >> n >> hp;
	for (int i = 0; i < n; i++) cin >> matrix[i][0] >> matrix[i][1];
	bt(0, 0);
	cout << ans;
}
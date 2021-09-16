#include <stdio.h>

int main1321312452151()
{
	int n;
	scanf_s("%d", &n);
	long long sum = 0;
	int ans = 1;
	while (sum < n)
	{
		sum += ans;
		ans += 1;
	}
	printf("%d", ans-1);
	return 0;
}
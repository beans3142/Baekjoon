#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);
	int y = 0;
	int m = 0;
	for (int i = 0; i < n; i++)
	{
		int num;
		scanf("%d", &num);
		y += num / 30 + 1;
		m += num / 60 + 1;
	}
	y *= 10;
	m *= 15;
	int ans = y < m ? y : m;
	if (y <= m)
	{
		printf("Y ");
	}
	if (m <= y)
	{
		printf("M ");
	}
	printf("%d", ans);
}
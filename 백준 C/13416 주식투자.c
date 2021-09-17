#include <stdio.h>
#include<math.h>

int main13416()
{
	int t;

	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		int n;
		scanf("%d", &n);
		int sum = 0;
		for (int j = 0; j < n; j++)
		{
			int a, b, c;
			scanf("%d %d %d", &a, &b, &c);
			sum += max(a, b, c, 0);
		}
		printf("%d", sum);
	}
	return 0;
}
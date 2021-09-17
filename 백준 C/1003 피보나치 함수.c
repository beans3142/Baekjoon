#include <stdio.h>

int main()
{
	int t;
	scanf("%d", &t);
	for (int j = 0; j < t; j++)
	{
		int a[2][41] = { 0, }; // -1 , 0, 1 ...
		a[0][0] = 1;
		a[1][1] = 1;
		int n;
		scanf("%d", &n);

		for (int i = 2; i < n+1; i++)
		{
			a[0][i] = a[0][i - 1] + a[0][i - 2];
			a[1][i] = a[1][i - 1] + a[1][i - 2];
		}
		printf("%d %d\n", a[0][n], a[1][n]);
	}
}
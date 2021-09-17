#include <stdio.h>

int main()
{
	double fac[31] = { 1, };
	int t;
	scanf("%d", &t);
	for (int i = 1; i < 31; i++)
	{
		fac[i] = fac[i - 1] * i;
	}
	for (int i = 0; i < t; i++)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		n = n < m - n ? n : m - n;
		printf("%.lf\n", (fac[m] / fac[m - n]) / fac[n]);
	}
	return 0;
}
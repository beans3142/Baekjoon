#include <stdio.h>

int fac(int x, int ans)
{
	return x > 1 ? fac((x - 1),ans*x) : ans;
}

int main()
{
	int n;
	scanf("%d", &n);
	printf("%d", fac(n,1));
}
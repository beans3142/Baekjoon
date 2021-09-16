#include <stdio.h>

int main()
{
	int a, b, n;
	scanf_s("%d %d %d",&a,&b,&n);
	a %= b;
	for (int i=0; i < n-1; i++)
	{
		a =a*10%b;
	}
	printf("%d\n", a);
	printf("%d", a *10 % b);
}
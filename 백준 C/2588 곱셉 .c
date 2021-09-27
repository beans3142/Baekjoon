#include <stdio.h>

int pow(int num, int mul, int left)
{
	if (left == 0)
	{
		return num;
	}
	pow(num * mul, mul, left - 1);
}

int main()
{
	int a, b;
	int ans = 0;
	scanf("%d %d", &a, &b);
	for (int i = 0; i < 3; i++)
	{
		printf("%d\n", a * (b % 10));
		ans += a * (b % 10)*pow(1,10,i);
		b /= 10;
	}
	printf("%d\n", ans);
}
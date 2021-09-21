#include <stdio.h>

int min(int num1, int num2)
{
	return num1 < num2 ? num1 : num2;
}

int main()
{
	int n, a, b;
	scanf("%d %d %d", &n, &a, &b);
	b -= a;

	for (int i = 0; i < 8-n; i++)
	{
		int x, y;
		scanf("%d %d", &x, &y);
		a += x * 3;
		b += min(6 - x,y)*3;
	}
	if (a > 65 && a+b > 129) printf("Nice");
	else printf("Nae ga wae");
}
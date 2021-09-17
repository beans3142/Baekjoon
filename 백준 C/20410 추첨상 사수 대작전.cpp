#include <stdio.h>

int main20410()
{
	int m, seed, x1, x2;
	int ans_a, ans_c;
	scanf_s("%d %d %d %d", &m, &seed, &x1, &x2);
	for (int a = 0; a < m; a++)
	{
		for (int c = 0; c < m; c++)
		{
			if ((a * seed + c) % m == x1)
			{
				if ((a * x1 + c) % m == x2) 
				{
					ans_a = a;
					ans_c = c;
					break;
				}
			}
		}
	}
	printf("%d %d", ans_a, ans_c);
	return 0;
}
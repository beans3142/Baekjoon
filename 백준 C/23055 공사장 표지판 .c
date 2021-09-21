#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);
	char sign[21][21];
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (i == 0 || i == n - 1 || j == 0 || j == n - 1)sign[i][j] = '*';
			else if (i == j || i == n - j - 1) sign[i][j] = '*';
			else sign[i][j] = ' ';
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			printf("%c", sign[i][j]);
		}
		printf("\n");
	}
}
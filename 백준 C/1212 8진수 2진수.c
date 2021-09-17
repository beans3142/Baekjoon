#include <stdio.h>
#include <string.h>

char s[333335];
char binary_s[1000001];

int main()
{
	int start = 0;
	scanf("%s", s);
	int s_len = strlen(s);
	for (int i = 0; i < s_len; i++)
	{
		int n = s[i] - '0';
		for (int j = 1; j < 4; j++)
		{
			binary_s[3 * (i + 1) - j] = n % 2;
			n /= 2;
		}
	}
	for (int i = 0; i < 3; i++)
	{
		start = i;
		if (binary_s[i] == 1)
		{
			break;
		}
	}
	for (int i = start; i < 3 * s_len; i++)
	{
		printf("%d", binary_s[i]);
	}
}
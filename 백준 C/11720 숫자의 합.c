#include <stdio.h>

int main()
{
	int n;
	int sum = 0;
	scanf("%d", &n);
	char s[101];
	scanf("%s", s);
	for (int i = 0; i < n; i++)
	{
		sum+=s[i] - '0';
	}
	printf("%d", sum);
}
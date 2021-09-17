#include <stdio.h>
#include <string.h>

char s[1000001];

int main()
{
	int cnt = 1;
	gets(s);
	int len = strlen(s);
	if (len == 1 && s[0] == ' ')
	{
		cnt--;
	}
	for (int i = 1; i < len - 1; i++)
	{
		if (s[i] == ' ')
		{
			cnt++;
		}
	}
	printf("%d", cnt);
}
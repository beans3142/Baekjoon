#include <stdio.h>

int min(int num1, int num2)
{
	return num1 > num2 ? num2 : num1;
}

int main()
{
	char s[1001];
	scanf("%s", s);
	int idx = 0;
	int key = 100;
	while (s[idx]!='\0')
	{
		key = min(key, s[idx++]-'A');
	}
	if (key > 2)
	{
		for (int i = 0; i < idx; i++) s[i] = 'A';
	}
	else
	{
		for (int i = 0; i < idx; i++)
		{
			if (s[i] - 'A' != 4 && s[i] - 'A' < 6)
			{
				s[i] = 'A' + key;
			}
		}
	}
	for (int i = 0; i < idx; i++)
	{
		printf("%c", s[i]);
	}
}
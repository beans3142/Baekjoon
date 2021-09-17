#include<stdio.h>
#include<string.h>

int main4470()
{
	int n;
	scanf("%d",&n);
	char v[1];
	gets(v);
	char str[51];
	for (int i = 0; i < n; i++)
	{
		scanf_s("%[^\n]s[' ']", str,sizeof(str));
		printf("%d. %s\n", i + 1, str);
	}
	return 0;
}
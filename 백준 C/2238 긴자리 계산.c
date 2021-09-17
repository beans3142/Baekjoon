#include <stdio.h>
#include <string.h>

int add[1001] = { 0 };
int mul[1000001] = { 0 };

int main()
{
	char a[1001];
	char b[1001];

	int a_len = strlen(a);
	for (int i = 0; i < a_len; i++)
	{
		add[a_len-i] = a[a_len-i]-'0';
		mul[a_len-i]=a
	}


}
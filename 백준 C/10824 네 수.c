#include <stdio.h>
#include <string.h>
#include<stdlib.h>
#include <math.h>

int main()
{
	char a[20];
	char b[20];
	char c[20];
	char d[20];
	long long ans;
	scanf("%s", a);
	scanf("%s", b);
	scanf("%s", c);
	scanf("%s", d);
	strcat(a, b);
	strcat(c, d);
	long long ab=0;
	long long cd = 0;
	int a_len = strlen(a);
	int c_len = strlen(c);
	for (int i = 0; i < a_len; i++)
	{
		ab += (a[a_len - 1 - i] - '0') * pow(10, i);
	}
	for (int i = 0; i < c_len; i++)
	{
		cd += (c[c_len - 1 - i] - '0') * pow(10, i);
	}
	printf("%lld", ab + cd);
}
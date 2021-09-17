#include <stdio.h>
#include <math.h>
#include <stdlib.h>

char a[50000];
char b[50000];
char reversed_a[50000];
char reversed_b[50000];
char total[100001] = { 0 };

void reverse(int len_a,int len_b)
{
	int idx_a = 0;
	int idx_b = 0;
	for (int i = len_a - 1; i >= 0; i--)
	{
		reversed_a[idx_a++] = a[i];
	}
	for (int i = len_b - 1; i >= 0; i--)
	{
		reversed_b[idx_b++] = b[i];
	}
	for (int i = 0; i < len_a; i++)
	{
		a[i] = reversed_a[i];
	}
	for (int i = 0; i < len_b; i++)
	{
		b[i] = reversed_b[i];
	}
}

int main()
{
	int len_a, len_b;
	int mx_len=0;

	scanf("%d %d", &len_a, &len_b);
	scanf("%s %s", a, b);
	reverse(len_a,len_b);
	for (int i = 0; i < len_a; i++)
	{
		for (int j = 0; j < len_b; j++)
		{
			int now = total[i+j] + (a[i]-'0') * (b[j]-'0');
			printf("%d\n", now);
			int over = now / 10;
			total[i + j + 1] = over+total[i+j+1];
			total[i + j] = now % 10;
		}
	}
	for (mx_len = len_a + len_b-1; total[mx_len] != 0; mx_len--);
	printf("%d\n", mx_len);
	for (int i = mx_len; i>0; i--)
	{
		printf("%d ", total[i]);
	}
}
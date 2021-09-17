#include <stdio.h>

int a[1000001] = {0,};

int max(int num1,int num2)
{
	return num1 > num2 ? num1 : num2;
}

int main()
{
	int n, b, c;
	long long ans = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%d",&a[i]);
	scanf("%d %d", &b, &c);
	for (int i = 0; i < n; i++)
	{
		ans += max(0, (a[i]-b)>0 ? (a[i]-b)/c+1 : 1);
		if ((a[i] - b) % c != 0 && a[i]-b>0)
		{
			ans++;
		}
	}
	printf("%lld", ans);
}
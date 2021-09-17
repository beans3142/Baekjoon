#include <stdio.h>

typedef long long ll;
ll lim_max = 9223372036854775807;
ll lim_min = -9223372036854775807;

int main()
{
	for (int i = 0; i < 3; i++)
	{
		int overflow = 0;
		long long sum = 0;
		int n;
		scanf_s("%d", &n);
		for (int j = 0; j < n; j++)
		{
			ll num;
			scanf("%lld", &num);
			if (num > 0)
			{
				if (sum >= lim_max - num)
				{
					sum = sum + (lim_max - num);
					overflow++;
				}
				else {
					sum += num;
				}
			}
			else if (num<0)
			{

				if (sum <= lim_min - num)
				{
					sum = sum - (lim_min - num);
					overflow--;
				}
				else {
					sum += num;
				}
			}
		printf("\n\nsum is %lld\n\n", sum);
		}
		if (overflow < 0)
		{
			printf("-\n");
		}
		else if (overflow > 0)
		{
			printf("+\n");
		}
		else
		{
			if (sum == 0)
			{
				printf("0\n");
			}
			else if (sum < 0)
			{
				printf("-\n");
			}
			else 
			{
				printf("+\n");
			}
		}
	}
}
#include <stdio.h>

int pow(int x,int n)
{
	if (n == 0)
	{
		return x;
	}
	return pow(x * 10, n-1);
}

int main()
{
	int price, money;
	scanf("%d %d", &price, &money); // Hello
	money = pow(1,money);
	printf("%d", (price+money/10*5)/money * money);
	//Hello? ぞしぞしぞ	  


	
}
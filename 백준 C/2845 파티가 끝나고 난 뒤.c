#include <stdio.h>

int main()
{
	int l, p;
	scanf("%d %d",&l,&p);
	for (int i = 0; i < 5; i++)
	{
		int num;
		scanf("%d", &num);
		printf("%d ",num-l*p);
	}
	return 0;
}
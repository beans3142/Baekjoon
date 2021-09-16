#include <stdio.h>

int main()
{
	int peace[6] = { 1,1,2,2,2,8 };
	for (int i = 0; i < 6; i++)
	{
		int n;
		scanf("%d",&n);
		printf("%d ", peace[i]-n);
	}
}
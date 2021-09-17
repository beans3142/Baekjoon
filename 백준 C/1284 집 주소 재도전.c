#include <stdio.h>
#include <string.h>

int main()
{
	int n_to_n[10] = { 4,2,3,3,3,3,3,3,3,3};
	while (1)
	{
		char sign[10000];
		scanf("%s", sign);
		int len = strlen(sign);
		if (sign == '0')
		{
			break;
		}
		/*if (len==1 && sign[0] == '0')
		{
			break;
		}*/
		int sum = len + 1;
		for (int i = 0; i < len; sum += n_to_n[sign[i++] - '0'])
		{
			continue;
		}
		printf("%d\n", sum);
	}
}
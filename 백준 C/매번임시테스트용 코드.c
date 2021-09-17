#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int d;
	scanf("%d", &d);
	int hwasung_galkkunikka = 0;
	for (int i = 0; i < d; i++)
	{
		int up_down;
		scanf("%d", &up_down);
		if (hwasung_galkkunikka == 0) n = (n * (100 + up_down)) / 100;
		if (n > 700)
		{
			hwasung_galkkunikka = 1;
		}
		//printf("%d\n",n);
	}
	if (hwasung_galkkunikka == 1) printf("I love musk");
	else printf("I hate musk");
	return 0;
}
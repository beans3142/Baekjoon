#include <stdio.h>

int main() {
	while (1)
	{
		int start_h,start_m,left_h,left_m;
		scanf("%d:%d %d:%d", &start_h, &start_m,&left_h,&left_m);
		start_m += start_h * 60;
		left_m += left_h * 60;
		if (start_m == 0 && left_m == 0) break;
		printf("%02d:%02d", (start_m + left_m) / 60 % 24, (start_m + left_m) % 60);
		if ((start_m + left_m) / 1440 > start_m / 1440) printf(" %d", (start_m + left_m) / 1440 - start_m / 1440);
		printf("\n");
	}
	return 0;
}
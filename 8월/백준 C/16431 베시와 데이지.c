#include <stdio.h>

int main16431()
{
	int b1, b2;
	int d1, d2;
	int j1, j2;

	scanf("%d %d", &b1, &b2);
	scanf("%d %d", &d1, &d2);
	scanf("%d %d", &j1, &j2);

	int lb = abs(j1 - b1)> abs(j2 - b2) ? abs(j1 - b1) : abs(j2 - b2); // 대각선으로도 이동이 가능하므로 b1 과 b2중 작은 값은 큰 값만큼 이동하는 도중 작은값만큼 대각선으로 이동하면 해결 됨!
	int ld = abs(d1 - j1) + abs(d2 - j2);
	if (lb == ld)
	{
		printf("tie");
	}
	else
	{
		printf(lb < ld ? "bessie" : "daisy");
	}
	return 0;
}
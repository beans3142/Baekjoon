#include <stdio.h>

int main16431()
{
	int b1, b2;
	int d1, d2;
	int j1, j2;

	scanf("%d %d", &b1, &b2);
	scanf("%d %d", &d1, &d2);
	scanf("%d %d", &j1, &j2);

	int lb = abs(j1 - b1)> abs(j2 - b2) ? abs(j1 - b1) : abs(j2 - b2); // �밢�����ε� �̵��� �����ϹǷ� b1 �� b2�� ���� ���� ū ����ŭ �̵��ϴ� ���� ��������ŭ �밢������ �̵��ϸ� �ذ� ��!
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
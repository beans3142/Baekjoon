#include <stdio.h>
#include <stdlib.h>

int arr[21] = { 0, };
int mk[1060000] = {0,};
int n;
int idx = 0;

int bt(int num,int left)
{
	for (int i = left; i < n; i++)
	{
		mk[idx++] = num+arr[i];
		bt(num + arr[i], i+1);
	}
	return 0;
}

int compare(const void* a, const void* b)    // �������� �� �Լ� ����
{
	int num1 = *(int*)a;    // void �����͸� int �����ͷ� ��ȯ�� �� �������Ͽ� ���� ������
	int num2 = *(int*)b;    // void �����͸� int �����ͷ� ��ȯ�� �� �������Ͽ� ���� ������

	if (num1 < num2)    // a�� b���� ���� ����
		return -1;      // -1 ��ȯ

	if (num1 > num2)    // a�� b���� Ŭ ����
		return 1;       // 1 ��ȯ

	return 0;    // a�� b�� ���� ���� 0 ��ȯ
}

int main()
{
	
	scanf("%d", &n);
	int len = (1 << n) - 1;
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}
	bt(0, 0);
	qsort(mk,len, sizeof(int), compare);
	int cnt = 1;
	for (int i = 1; i < len; i++)
	{
		if (mk[i] != mk[i - 1]) cnt++;
	}
	printf("%d", mk[len-1] - cnt);
}
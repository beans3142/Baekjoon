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

int compare(const void* a, const void* b)    // 오름차순 비교 함수 구현
{
	int num1 = *(int*)a;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴
	int num2 = *(int*)b;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴

	if (num1 < num2)    // a가 b보다 작을 때는
		return -1;      // -1 반환

	if (num1 > num2)    // a가 b보다 클 때는
		return 1;       // 1 반환

	return 0;    // a와 b가 같을 때는 0 반환
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
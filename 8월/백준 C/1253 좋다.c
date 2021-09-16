#include <stdio.h>
#include <stdlib.h>

int cmp(int *a,int *b)
{
	int num1 = *a;
	int num2 = *b;
	if (num1 > num2) return 1;
	else if (num2 > num1) return -1;
	return 0;
}

int main()
{
	int n;
	int arr[2000];
	int cnt = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int num;
		scanf("%d", &num);
		arr[i] = num;
	}
	qsort(arr, n, sizeof(int), cmp);
	//for (int i = 0; i < n; printf("%d ", arr[i++]));
	for (int i = 0; i < n; i++)
	{
		int l = 0;
		int r = n - 1;
		while (l < r)
		{
			if (l == i)
			{
				l++;
			}
			if (r == i)
			{
				r--;
			}
			if (l >= r) break;
			int sum = arr[l] + arr[r];
			//printf("%d ", sum);
			if (sum == arr[i])
			{
				cnt++;
				break;
			}
			if (sum<arr[i])
			{
				l++;
			}
			else
			{
				r--;
			}
		}
	}
	printf("%d", cnt);
}
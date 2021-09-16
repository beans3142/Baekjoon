#include <stdio.h>

int min(int num1, int num2)
{
	return num1 > num2 ? num2 : num1;
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
	{
		int n,m;
		int room[101][101];
		int person[101];
		scanf("%d %d", &n, &m);
		for (int i = 0; i <= n; i++) // 101*101 ũ���� 2���� �迭 ���� ���� ä����
		{
			for (int j = 0; j <= n; j++)
			{
				room[i][j] = 10000000;
			}
		}
		for (int i = 0; i < m; i++) //m���� �� �Է�
		{
			int a, b, c;
			scanf("%d %d %d", &a,&b,&c);
			room[a][b] = c;
			room[b][a] = c;
		}
		for (int i = 1; i <= n; i++) //�÷��̵� �ͼ��� ����Ǿ� �ִ� �� ���� �Ÿ��� ������
		{
			room[i][i] = 0;
			for (int j = 1; j <= n; j++)
			{
				for (int k = 1; k <= n; k++)
				{
					room[j][k] = min(room[j][i]+room[i][k],room[j][k]);
				}
			}
		}
		int mn = 100000000;
		int ans = 0;
		int k;
		scanf("%d", &k); // K���� ģ�� �Է�

		for (int i = 0; i < k; i++)
		{
			int friend;
			scanf("%d", &friend);
			person[i] = friend;
		}

		for (int i = 1; i <= n; i++)
		{
			int total_dist=0;
			for (int j = 0; j < k; j++)
			{
				total_dist += room[i][person[j]];
			}
			if (total_dist < mn)
			{
				ans = i;
				mn = total_dist;
			}
		}
		printf("%d\n", ans);
	}
}
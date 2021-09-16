#include<stdio.h>
#include<string.h>

int n, m, k;  // ���� ����
int map[50][50];

void dfs(int a, int b) {  // ���� ����

	map[a][b] = 0; // �湮�Ѱ� ����
	if (map[a][b + 1] == 1 && b + 1 < m) {  // ��
		dfs(a, b + 1);
	}
	if (map[a][b - 1] == 1 && b - 1 >= 0) { // ��
		dfs(a, b - 1);
	}
	if (map[a - 1][b] == 1 && a - 1 >= 0) { // ��
		dfs(a - 1, b);
	}
	if (map[a + 1][b] == 1 && a + 1 < n) { // ��
		dfs(a + 1, b);
	}
}

int main() {

	int test;
	scanf("%d", &test);

	while (test--) {

		memset(map, 0, 51);
		scanf("%d %d %d", &m, &n, &k); // ���� ���� ����

		int x, y;
		while (k--) {
			scanf("%d %d", &x, &y);  // x = ����  y=����

			map[y][x] = 1;
		}

		int cnt = 0;
		for (int i = 0; i < n; i++) {  //����
			for (int j = 0; j < m; j++) {  //����
				if (map[i][j] == 1) {
					dfs(i, j);  // ���� ����
					cnt++;
				}
			}
		}

		printf("%d\n", cnt);
	}

}
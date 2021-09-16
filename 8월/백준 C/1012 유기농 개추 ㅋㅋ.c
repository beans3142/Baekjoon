#include<stdio.h>
#include<string.h>

int n, m, k;  // 세로 가로
int map[50][50];

void dfs(int a, int b) {  // 세로 가로

	map[a][b] = 0; // 방문한거 제거
	if (map[a][b + 1] == 1 && b + 1 < m) {  // 동
		dfs(a, b + 1);
	}
	if (map[a][b - 1] == 1 && b - 1 >= 0) { // 서
		dfs(a, b - 1);
	}
	if (map[a - 1][b] == 1 && a - 1 >= 0) { // 남
		dfs(a - 1, b);
	}
	if (map[a + 1][b] == 1 && a + 1 < n) { // 북
		dfs(a + 1, b);
	}
}

int main() {

	int test;
	scanf("%d", &test);

	while (test--) {

		memset(map, 0, 51);
		scanf("%d %d %d", &m, &n, &k); // 가로 세로 간선

		int x, y;
		while (k--) {
			scanf("%d %d", &x, &y);  // x = 가로  y=세로

			map[y][x] = 1;
		}

		int cnt = 0;
		for (int i = 0; i < n; i++) {  //세로
			for (int j = 0; j < m; j++) {  //가로
				if (map[i][j] == 1) {
					dfs(i, j);  // 세로 가로
					cnt++;
				}
			}
		}

		printf("%d\n", cnt);
	}

}
#include <stdio.h>

char matrix[1201][1201];
int dx[4] = {0,0,-1,1};
int dy[4] = { 1,-1,0,0 };

int main()
{
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n*3; i++)
	{
		scanf("%s",matrix[i]);
	}
	for (int i = 0; i < n ; i++)
	{
		for (int j = 0; j < m; j++)
		{
			int x = j * 3 + 1;
			int y = i * 3 + 1;
			for (int d = 0; d < 4; d++)
			{
				int nx = x + dx[d];
				int ny = y + dy[d];
				if (matrix[ny][nx] == '#')
				{
					for (int k = 0; k < 2; k++)
					{
						ny += dy[d];
						nx += dx[d];
						matrix[ny][nx] = '#';
					}
				}
			}
		}
	}

	for (int i = 0; i < n*3; i++)
	{
		for (int j = 0; j < m*3; j++)
		{
			printf("%c", matrix[i][j]);
		}
		printf("\n");
	}
}
/*
4 4
............
.##...###...
.#..........
....#.....#.
....#.....#.
....#.....#.
.#.....#....
.##....#....
.#.....#....
....#.....#.
...###...##.
............

2 4
............
.##...###...
.#..........
....#.....#.
...###...##.
............
*/

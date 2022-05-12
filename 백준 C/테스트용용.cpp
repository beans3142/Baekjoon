#include <iostream>
#include <cstdio>
#include <vector>
#include <memory.h>

#define max(a,b)(a > b ? a : b)
#define MAX_N 102
#define MAX_V 1002
using namespace std;

vector<int> adj[MAX_V];
vector<int> aMatch;
vector<int> bMatch;

int map[MAX_N][MAX_N];
int visit[MAX_V];
int visitCnt;

int Left[MAX_N][MAX_N];
int Right[MAX_N][MAX_N];

int n, m;

void fillLeft();
void fillRight();
void checkLeftandRight();

bool dfs(int a)
{
    if (visit[a] == visitCnt)
        return false;

    visit[a] = visitCnt;

    for (int next = 0; next < adj[a].size(); next++)
    {
        int b = adj[a][next];

        if (bMatch[b] == -1 || dfs(bMatch[b]))
        {
            aMatch[a] = b;
            bMatch[b] = a;

            return true;
        }
    }

    return false;
}

int bipartiteMatch()
{
    aMatch = vector<int>(n + 1, -1);
    bMatch = vector<int>(m + 1, -1);

    int size = 0;

    for (int a = 1; a <= n; a++)
    {
        visitCnt++;
        size += dfs(a);
    }

    return size;
}

int main()
{
    scanf("%d", &n);

    int t;
    scanf("%d", &t);

    // 영역에 포함되지 않는 부분은 -1로 초기화
    memset(map, -1, sizeof(map));

    // 영역을 모두 1로 초기화
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            map[i][j] = 1;

    // 벽을 모두 0으로 갱신
    for (int i = 0; i < t; i++)
    {
        int y, x;
        scanf("%d %d", &y, &x);
        map[y][x] = 0;
    }
    fillLeft();
    fillRight();
    // checkLeftandRight();

    checkLeftandRight();

    // 1일때만 간선 연결(0일때는 벽이니)
    int maxL = 0, maxR = 0;

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (map[i][j] == 1)
            {
                adj[Left[i][j]].push_back(Right[i][j]);

                maxL = max(maxL, Left[i][j]);
                maxR = max(maxR, Right[i][j]);
            }

    // 이분매칭에 이용 될 n과 m은 maxL, maxR로 교체된다.
    n = maxL;
    m = maxR;

    int get = bipartiteMatch();
    printf("%d", get);

    return 0;
}


void fillLeft()
{
    int y = 1;
    int x = n;
    int cnt = 1;

    // 오른쪽 위 시작 기준 대각선은 총 n번 반복
    for (int k = 0; k < 2 * n - 1; k++)
    {
        int tmpy = y;
        int tmpx = x;
        bool chk = false;

        while (tmpy <= n)
        {
            if (map[tmpy][tmpx] != -1)
            {
                if (map[tmpy][tmpx] == 1)
                {
                    Left[tmpy][tmpx] = cnt;
                    chk = true;
                }
                else
                    if (chk)
                    {
                        cnt++;
                        chk = false;
                    }
            }

            tmpy++;
            tmpx++;
        }

        if (chk)
        {
            cnt++;
            chk = false;
        }

        x--;
    }
}

void fillRight()
{
    int y = n;
    int x = n;
    int cnt = 1;

    // 오른쪽 아래 시작 기준 대각선은 총 n번 반복
    for (int k = 0; k < 2 * n - 1; k++)
    {
        int tmpy = y;
        int tmpx = x;
        bool chk = false;

        while (tmpy > 0)
        {
            if (map[tmpy][tmpx] != -1)
            {
                if (map[tmpy][tmpx] == 1)
                {
                    Right[tmpy][tmpx] = cnt;
                    chk = true;
                }
                else
                    if (chk)
                    {
                        cnt++;
                        chk = false;
                    }
            }

            tmpy--;
            tmpx++;
        }
        if (chk)
        {
            cnt++;
            chk = false;
        }

        x--;
    }
}

void checkLeftandRight()
{
    cout << endl;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            cout << Left[i][j] << " ";
        cout << endl;
    }

    cout << endl;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            cout << Right[i][j] << " ";
        cout << endl;
    }

    cout << endl;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            cout << map[i][j] << " ";
        cout << endl;
    }
}
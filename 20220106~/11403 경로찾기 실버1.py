import sys
input=sys.stdin.readline

n=int(input())
matrix=[list(map(int,input().split())) for i in range(n)]

def dfs(x):
    global visited
    for i in range(n):
        if matrix[x][i]==1 and visited[i]=='0':
            visited[i]='1'
            dfs(i)
    

for i in range(n):
    visited=['0']*n
    dfs(i)
    print(' '.join(visited))



import sys
input=sys.stdin.readline

n,m=map(int,input().split())
matrix={i:[]for i in range(1,n+1)}
visited={i:0 for i in range(1,n+1)}
gaesu=0

def dfs(x):
    global visited
    visited[x]=1
    for j in matrix[x]:
        try:
            if visited[j]==0:
                dfs(j)
        except RecursionError:
            return

for i in range(m):
    a,b=map(int,input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for i in matrix:
    if visited[i]==0:
        dfs(i)
        gaesu+=1

print(gaesu)

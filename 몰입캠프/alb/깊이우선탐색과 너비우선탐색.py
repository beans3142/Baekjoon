from sys import stdin
from collections import deque
input=stdin.readline

dfs_result=[]
bfs_result=[]

n,m=map(int,input().split())
graph=[[] for i in range(n)]
v=[[0 for i in range(n)]for i in range(2)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i]=sorted(graph[i])

def dfs(x):
    v[0][x]=1
    dfs_result.append(x)
    for i in graph[x]:
        if v[0][i]==0:
            dfs(i)

def bfs(x):
    queue=deque([x])
    while queue:
        now=queue.popleft()
        if v[1][now]!=0:
            continue
        bfs_result.append(now)
        v[1][now]=1
        for i in graph[now]:
            if v[1][i]==0:
                queue.append(i)

dfs(0)
bfs(0)

print(*dfs_result)
print(*bfs_result)

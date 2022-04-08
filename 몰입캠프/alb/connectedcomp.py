from sys import stdin
from collections import deque
input=stdin.readline

# 연결요소의 갯수, dfs bfs 뭐든 돌려서 탐색하고 모두 표시해주면 됨
# 다 탐색하기 까지 dfs나 bfs를 몇번 돌려야 하는지 문제

v,e=map(int,input().split())
graph=[[] for i in range(v+1)]
vi=[0]*(v+1)
cnt=0

for i in range(e):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def bfs(x):
    queue=deque([x])
    vi[x]=1
    while queue:
        now=queue.popleft()
        for i in graph[now]:
            if vi[i]==1:
                continue
            vi[i]=1
            queue.append(i)
    
for i in range(1,v+1):
    if vi[i]==0:
        cnt+=1
        bfs(i)

print(cnt)

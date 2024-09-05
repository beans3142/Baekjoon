from sys import stdin
from collections import deque
input=stdin.readline

n,m,k,x=map(int,input().split())
graph=[[] for i in range(n+1)]
vi=[-1]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

vi[x]=0
queue=deque([x])

while queue:
    now=queue.popleft()
    if vi[now]==k+1:
        break
    for nxt in graph[now]:
        if vi[nxt]==-1:
            vi[nxt]=vi[now]+1
            queue.append(nxt)

if k in vi:
    for i in range(n+1):
        if vi[i]==k:
            print(i)
else:
    print(-1)

from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
color=[0]*(n+1)
color[1]=1
able=True

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue=deque([1])
while queue:
    now=queue.popleft()
    for i in graph[now]:
        if color[i]==color[now]:
            able=False
        if color[i]==0:
            color[i]=-color[now]
            queue.append(i)
if able:
    print("Yes")
else:
    print("No")

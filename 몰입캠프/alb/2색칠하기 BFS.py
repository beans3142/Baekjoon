from collections import deque
from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
graph=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
queue=deque([(0,1)])
v=[0]*n
v[0]=1
able=True
while queue:
    now,color=queue.popleft()
    nextcolor=2 if color==1 else 1
    for i in graph[now]:
        if v[i]==color:
            able=False
        if v[i]!=0:
            continue
        v[i]=nextcolor
        queue.append([i,nextcolor])

if able:
    print("YES")
else:
    print("NO")

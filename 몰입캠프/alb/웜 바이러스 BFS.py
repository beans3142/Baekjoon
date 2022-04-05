from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]
v=[0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue=deque([1])
v[1]=1

while queue:
    now=queue.popleft()
    for i in graph[now]:
        if v[i]==0:
            v[i]=1
            queue.append(i)

print(sum(v)-1)

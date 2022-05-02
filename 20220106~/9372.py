from sys import stdin
from collections import deque
input=stdin.readline

def bfs(x):
    vi=[0]*(n+1)
    vi[x]=1
    queue=deque([x])
    cnt=0
    while queue:
        now=queue.popleft()
        for i in graph[now]:
            if vi[i]==0:
                vi[i]=1
                cnt+=1
                queue.append(i)

    return cnt


t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]

    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(bfs(1))

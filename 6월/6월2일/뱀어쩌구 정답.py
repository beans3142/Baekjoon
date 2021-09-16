from collections import deque

n, m=map(int, input().split())
k=101
g=[*range(k)]
dist=[-1]*k

for i in range(n+m) :
    x, y=map(int, input().split())
    g[x]=y

q=deque()
dist[1]=0
q.append(1)
while q :
    x=q.popleft()
    for i in range(1, 7) :
        y=x+i
        if(y>100) :
            continue
        y=g[y]
        if(dist[y]==-1 or dist[y]>dist[x]+1) :
            dist[y]=dist[x]+1
            q.append(y)

print(dist[-1])

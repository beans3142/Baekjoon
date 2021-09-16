from sys import stdin
from heapq import heappop,heappush
input=stdin.readline

n,m=map(int,input().split())
nxt={i:[] for i in range(1,n+1)}
level={i:0 for i in range(1,n+1)}
queue=[]
ans=[]

for i in range(m):
    a,b=map(int,input().split())
    nxt[a].append(b)
    level[b]+=1

for i in level:
    if level[i]==0:
        heappush(queue,i)

while queue:
    now=heappop(queue)
    ans.append(now)
    for i in nxt[now]:
        level[i]-=1
        if level[i]==0:
            heappush(queue,i)

print(*ans)

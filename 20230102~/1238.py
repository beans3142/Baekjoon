from sys import stdin
from collections import defaultdict
from heapq import heappop,heappush
input=stdin.readline

inf=float('inf')

def dijk(place):
    dist=[inf]*(n+1)
    dist[x]=0
    hq=[(0,x)]
    while hq:
        nowcost,nowloc=heappop(hq)
        for nxt in place[nowloc]:
            nxtcost=nowcost+place[nowloc][nxt]
            if nxtcost<dist[nxt]:
                dist[nxt]=nxtcost
                heappush(hq,(nxtcost,nxt))
    return dist
    

n,m,x=map(int,input().split())
vil=[defaultdict(int) for i in range(n+1)]
rev_vil=[defaultdict(int) for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    vil[a][b]=c
    rev_vil[b][a]=c

from_home=dijk(vil)
from_x=dijk(rev_vil)

ans=0
for i in range(n):
    ans=max(ans,from_home[i+1]+from_x[i+1])

print(ans)

# 단방향 그래프임을 이용
# 방향을 뒤집고 철수의 집에서 다익스트라를 돌리면 철수의 집으로 오는 거리.
# 뒤집지 않고 철수의 집에서 다익스트라를 돌리면 철수의 집에서 돌아가는 거리.
# 입력을 받을 때 뒤집은 그래프와 뒤집지 않은 그래프를 2개 만들어준뒤
# 각각 다익스트라를 돌려서 거리를 구한뒤 합쳐서 출력해준다.

from sys import stdin
from collections import defaultdict
from heapq import *

inf=float('inf')
n,m,k=map(int,input().split())
comeparty={i:defaultdict(int) for i in range(1,n+1)}
backhome={i:defaultdict(int) for i in range(1,n+1)}

for i in range(m):
    a,b,c=map(int,input().split())
    comeparty[b][a]=c if comeparty[b][a]==0 else min(comeparty[b][a],c)
    backhome[a][b]=c if backhome[a][b]==0 else min(backhome[a][b],c)
    
def dijk(s,party):
    dist=[inf]*(n+1)
    dist[0]=dist[s]=0
    queue=[(0,s)]
    while queue:
        totaldist,now=heappop(queue)
        if dist[now]<totaldist:
            continue
        for i in party[now]:
            nxtdist=totaldist+party[now][i]
            if dist[i]>nxtdist:
                dist[i]=nxtdist
                heappush(queue,(nxtdist,i))
    return dist

come=dijk(k,comeparty)
back=dijk(k,backhome)

print(sum(come)+sum(back))

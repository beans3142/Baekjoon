from sys import stdin
from heapq import heappop,heappush
from collections import defaultdict
input=stdin.readline

def dijk():
    inf=float('inf')
    hq=[(0,0,a)]
    cost=[inf]*(n+1)
    cost[a]=0
    while hq:
        totalcost,nowcost,nowloc=heappop(hq)
        for nxt in graph[nowloc]:
            nxtcost=max(nowcost,graph[nowloc][nxt])
            nxttotalcost=totalcost+graph[nowloc][nxt]
            if nxtcost<cost[nxt] and nxttotalcost<=c:
                cost[nxt]=nxtcost
                heappush(hq,(nxttotalcost,nxtcost,nxt))
    return cost[b]
        
def solve_bt():
    vi=[0]*(n+1)
    vi[a]=1
    ans=10e9
    def bt(nowcost,totalcost,now):
        nonlocal ans
        if now==b:
            ans=min(ans,nowcost)
            return
        for nxt in graph[now]:
            if vi[nxt]==0:
                nxtcost=max(nowcost,graph[now][nxt])
                nxttotalcost=totalcost+graph[now][nxt]
                if nxttotalcost<=c:
                    vi[nxt]=1
                    val=bt(nxtcost,nxttotalcost,nxt)
                    vi[nxt]=0
    bt(0,0,a)
    
    return ans
                
        
    

n,m,a,b,c=map(int,input().split())
graph=[defaultdict(int) for i in range(n+1)]

for i in range(m):
    x,y,v=map(int,input().split())
    graph[x][y]=v
    graph[y][x]=v
    

ans=dijk()
#ans=solve_bt()
print(ans if ans<=c else -1)

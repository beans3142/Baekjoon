from collections import deque
from sys import stdin
input=stdin.readline

inf=float('inf')

def bellman_ford(graph,edgeCnt,nodeCnt):
    distance=[inf]*(n+1)
    start=1
    distance[start]=0
    queue=deque([(0,start)])
    ans=[]
    isCycle=False
    for step in range(1,nodeCnt+1):
        le=len(queue)
        for nowNode in range(1,nodeCnt+1):
            for nxtNode,cost in graph[nowNode]:
                nxtCost=distance[nowNode]+cost
                if distance[nxtNode]>nxtCost:
                    distance[nxtNode]=nxtCost
                    queue.append((nxtCost,nxtNode))
        if step==nodeCnt-1:
            ans=distance[:]
        elif step==nodeCnt:
            if ans!=distance:
                isCycle=True
    if isCycle:
        return -1
    return distance
    

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

result=bellman_ford(graph,m,n)
if result==-1:
    print(result)
else:
    for i in result[2:]:
        print(i if i!=inf else -1)

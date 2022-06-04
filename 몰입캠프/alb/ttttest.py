## template
import heapq

n,m=map(int,input().split())

inf=float('inf')

graph=[[]for i in range(n+1)]

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))
  
p1,p2=map(int,input().split())
  
def dijkstra(start,end):
  distance=[inf for _ in range(n+1)]
  hq=[]
  distance[start]=0
  heapq.heappush(hq,(0,start))
  while hq:
    dist,now=heapq.heappop(hq)
    if distance[now]<dist:
      continue
    for nxt in graph[now]:
      cost=dist+nxt[1]
      if distance[nxt[0]]>cost:
        distance[nxt[0]]=cost 
        heapq.heappush(hq,(cost,nxt[0]))
  return distance[end]
  
path1=dijkstra(1,p1)+dijkstra(p1,p2)+dijkstra(p2,n)
path2=dijkstra(1,p2)+dijkstra(p2,p1)+dijkstra(p1,n)

print(min(path1,path2))
  

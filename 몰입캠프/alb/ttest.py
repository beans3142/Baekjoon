from heapq import heappop,heappush
from sys import stdin
input=stdin.readline

n,m=map(int,input().split())

# 딕셔너리를 이용한 구현
graph=[{} for i in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    try:
        graph[a][b]=graph[b][a]=min(graph[a][b],c)
    except:
        graph[a][b]=graph[b][a]=c

def dijkstra(start,end): # 다익스트라 알고리즘
    inf=float('inf') # 큰 수
    value=[inf]*(n+1) # 비용 배열
    value[start]=0
    pq=[(0,start)] # 비용, 노드 이런 식으로 저장해주어야 합니다!
    while pq:
        nowvalue,nownode=heappop(pq) # 큐에서 비용이 최소인 값들 추출 합니다.
        if value[nownode]<nowvalue: # ⓐ 같은 노드가 두 번 들어갈 수 있습니다!
            continue
        # 아래 코드는 만약 끝까지 거리만 알아도 될 경우 주석해제 해주시면 됩니다!
        '''
        if nownode==end:
            return value
            '''
        for nextnode in graph[nownode]: # 현재 노드에서 갈 수 있는 노드들입니다.
            nextvalue=nowvalue+graph[nownode][nextnode] # 누적 가중치에 현재 가중치를 더해줍니다.
            if nextvalue<value[nextnode]: # 누적 가중치 비교
                value[nextnode]=nextvalue # 누적 가중치가 적다면 저장
                heappush(pq,(nextvalue,nextnode)) # push
    return value

a,b=map(int,input().split())

# 매번 다익스트라를 
from_start=dijkstra(1,n)
from_a=dijkstra(a,n)
from_b=dijkstra(b,n)

start_a_b_end=from_start[a]+from_a[b]+from_b[n]
start_b_a_end=from_start[b]+from_b[a]+from_a[n]

print(min(start_a_b_end,start_b_a_end))
            
        

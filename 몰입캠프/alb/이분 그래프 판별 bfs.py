from sys import stdin
from collections import deque
input=stdin.readline

def bfs(start):
    
    dist=[-1]*(n+1) # 거리를 저장해줄 배열 (미방문은 -1 로 초기화)
    dist[1]=0 # n의 범위가 2 ~ 1000 까지 이므로 1은 n이 어떤 값이든 항상 존재하므로

    queue=deque([start]) # 전달해준 시작점을 넣는다.
    
    while queue: # BFS
        now=queue.popleft()
        for nextnode in graph[now]: # 현재 노드에서 갈 수 있는 노드들
            if dist[nextnode]==-1: # 미방문 노드라면
                # 미방문인 지점 넣기 전에 방문처리
                # 이 과정을 통해서 BFS 이용시 중복방문을 없앨 수 있다.
                dist[nextnode]=dist[now]+1

                # 큐에 값 추가
                queue.append(nextnode)
            elif dist[nextnode]%2==dist[now]%2: # 미방문 노드가 아닌데 방문 홀짝이 같다면
                # nextnode와 now는 연결되어 있는데 이동 거리가 같다면
                # nextnode에서 now로 이동하는데 거리가 +1 이므로 이분 그래프가 아니게 된다.
                return False
        
    return True

def dfs(nownode,dist):
    

n,m=map(int,input().split())
graph=[[] for i in range(n+1)] # 그래프는 1~n+1

able=True # 가능 불가능 함수 사용 시 return True로 대체 가능

for i in range(m): # 인접리스트로 그래프 구현
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



if able:
    print("Yes")
else:
    print("No")

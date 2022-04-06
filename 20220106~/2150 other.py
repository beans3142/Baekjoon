# c++ 기준 해설을 보고 파이썬으로 바꿔 짠 코드
from sys import stdin,setrecursionlimit
setrecursionlimit(100000)
input=stdin.readline

def get_my_group(node): # 해당 노드와 같은 그룹의 모든 정점을 알 수 있다.
    check2[node]=1
    group[node]=group_cnt
    group_reversed[group_cnt].append(node)
    for nextnode in graph_reversed[node]:
        if check2[nextnode]==0:
            get_my_group(nextnode)
        

def get_time(node): # 시간 배열 얻는 함수
    global clock,order_idx
    check[node]=1 # 해당 노드 방문처리
    for nextnode in graph[node]: # 인접 노드 탐색
        if check[nextnode]==0: # 인접 노드 중 방문하지 않은 곳 있다면 방문
            get_time(nextnode)

    time[node]=clock # 인접 노드를 전부 탐색 후 clock 저장
    order[order_idx]=node # 현재 order_idx에 맞게 node 저장
    clock+=1 # clock 값 증가
    order_idx+=1 # order_idx 값 증가

if __name__ == "__main__":
    # 정점의 개수와 간선의 개수 입력받기
    n,m=map(int,input().split()) # n : 정점의 개수, m : 간선의 개수

    # 그래프 선언하기
    graph=[[]for i in range(n+1)] # 원래 형태의 그래프
    graph_reversed=[[] for j in range(n+1)] # 방향이 반대가 된 그래프

    # 그래프 완성하기
    for i in range(m): # 간선의 개수 만큼 입력받음
        a,b=map(int,input().split())
        graph[a].append(b)
        graph_reversed[b].append(a)

    # DFS를 하면서 빠져나온 시간을 저장해줄 배열과 초기 시작 시간을 선언
    time=[0 for i in range(n+1)] # 시간 저장
    order=[0 for i in range(n+1)] # DFS 후 나온 순서 저장
    order_idx=1
    clock=1 # 맨 처음 시간, DFS를 통해 증가시켜줄 값
    check=[0 for i in range(n+1)] # get_time 함수 방문처리
    check2=[0 for i in range(n+1)] # DFS 방문처리
    group=[0 for i in range(n+1)] # 정점 i가 속한 그룹 번호 저장
    group_cnt=1 # 그룹 번호
    group_reversed=[[] for i in range(n+1)] # 그룹 번호에 속한 정점 저장
    for idx in range(1,n+1):
        if check[idx]==0: # 아직 방문하지 않았다면
            get_time(idx)

    for idx in range(order_idx-1,0,-1):
        node=order[idx]
        if check2[node]==0:
            get_my_group(node)
            group_reversed[group_cnt].sort()
            group_cnt+=1

    print(group_cnt-1) # 그룹의 개수 출력 1부터 출력하므로 -1
    for i in sorted(group_reversed):
        if i!=[]:
            print(*i,-1)

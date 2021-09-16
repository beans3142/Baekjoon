# dp로 예상됨.
# 뒤로 가는거 없음.
# bfs? 로 풀 수 있을 듯?

import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
visited=[0]+[1000 for i in range(n-1)] # 1번째는 무조건 0,

def jump():
    queue=deque([[arr[0],0,0]]) # arr[0]번째 값(이동가능거리),현재위치,현재이동횟수
    while queue:
        can,idx,tmpt=queue.popleft()
        for i in range(1,can+1): # 이동 가능 거리만큼 반복
            if idx+i<n: # n까지 이므로, 범위 밖으로 안나가게
                if tmpt+1<visited[idx+i]:
                    visited[idx+i]=tmpt+1
                    queue.append([arr[idx++i],idx+i,tmpt+1])
jump()
print(visited[-1] if visited[-1]!=1000 else -1)     

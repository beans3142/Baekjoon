from sys import stdin
from collections import deque
input=stdin.readline

# 구름의 이동 구현을 잘해야할 것 같다.
# ex) 기존에 흔히 보이던 이동 방식과 달리 격자 밖으로 넘어가면 반대편에서

# 이동 방향 순서대로
move=[[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
daegak=[[1,1],[1,-1],[-1,1],[-1,-1]]

# 입력값들 입력받기
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
cloud=deque([[0,n-1],[0,n-2],[1,n-1],[1,n-2]]) # 초기 구름의 위치
rained=[[0 for i in range(n)] for i in range(n)] # 이동 횟수를 이용하여 비가 온 지역 구분

order=[] # M번의 이동 명령 넣어줄 곳

# M번의 이동 명령 저장
for i in range(m):
    order.append(list(map(int,input().split())))

for now in range(m):
    head=order[now][0] # 방향
    dist=order[now][1] # 거리
    moved=[] # 구름이 이동한 곳들의 위치 저장
    for x,y in cloud:
        # n칸 이동시 제자리이므로 %n 이용
        nx=(x+move[head-1][0]*dist)%n
        nx=nx if nx>=0 else n+nx
        ny=(y+move[head-1][1]*dist)%n
        ny=ny if ny>=0 else n+ny
        # nx,ny는 이동한 위치를 갖음
        moved.append([nx,ny])
    
    cloud=[]
    for x,y in moved:
        # 비가 내린 지역이므로 +1
        arr[y][x]+=1
        rained[y][x]=now+1 # 그냥 now로 하면 맨 처음 초기화한 값이 0 이고 초기값이 0으로 겹치므로
        # 대각선의 물 체크
    for x,y in moved:
        for _ in range(4):
            nx=x+daegak[_][0]
            ny=y+daegak[_][1]
            if -1<nx<n and -1<ny<n: # 물이 들어있는지 체크는 격자 범위 벗어남 X
                if arr[ny][nx]!=0: # 물이 차있다면
                    arr[y][x]+=1 # 1씩 더해줌

    # 물의 양이 2 이상인 곳 찾고 구름에 넣어주기
    for y in range(n):
        for x in range(n):
            if rained[y][x]!=now+1 and arr[y][x]>1:
                arr[y][x]-=2
                cloud.append([x,y])
                
                
print(sum([sum(i) for i in arr]))

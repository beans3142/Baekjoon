from sys import stdin
input=stdin.readline
from collections import deque

dr=[0,0,1,-1]
dc=[1,-1,0,0]

def getMisfortune(r1,c1,r2,c2,r3,c3):
    return arr[r1][c1]+arr[r2][c2]+arr[r3][c3]


n,m,k=map(int,input().split())
arr=[list(input().rstrip()) for i in range(n)]

# 필요한 좌표 전처리, 정수로 바꿔줌, X는 -1 시작 끝점은 0으로
sr,sc,er,ec=0,0,0,0
for i in range(n):
    for j in range(m):
        if arr[i][j]=='S':
            sr,sc=i,j
            arr[i][j]=0
        elif arr[i][j]=='H':
            er,ec=i,j
            arr[i][j]=0
        elif arr[i][j]=='X':
            arr[i][j]=-1
        else:
            arr[i][j]=int(arr[i][j])


# 큐 생성
# 큐에 어떻게 넣을까...
# 지금, 전, 전전, 이동횟수 넣었다
queue=deque([(sr,sc,sr,sc,0,0)])
vi=set()

while queue:
    nowr,nowc,befr,befc,curmove,fsum=queue.popleft()
    for i in range(4):
        # 다음 좌표
        nxtr=nowr+dr[i]
        nxtc=nowc+dc[i]
        # 좌표 범위 체크
        if -1<nxtr<n and -1<nxtc<m:
            # X (-1) 이면 continue
            if arr[nxtr][nxtc]==-1: continue
            # 되돌아가는 경우 continue
            if befr==nxtr and befc==nxtc: continue

            
            # 누적 불운 ( 좌표 3개로 계산 )
            nxtmisfort=fsum+arr[nxtr][nxtc]
            # 누적 불운이 k초과면 continue
            if nxtmisfort>k: continue
            if nxtr==er and nxtc==ec:
                print(curmove+1)
                exit()
            

            # 방문처리를 위한 key 생성
            # bef는 신경쓰지 않아도 된다.
            key=(nxtr,nxtc,nowr,nowc)
            if key in vi: continue
            vi.add(key)
            queue.append((nxtr,nxtc,nowr,nowc,curmove+1,fsum-(arr[befr][befc] if curmove>2 else 0)))
    

print(-1)

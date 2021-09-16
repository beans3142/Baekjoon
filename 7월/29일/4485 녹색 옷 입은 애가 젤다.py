import sys
from heapq import heappop,heappush
input=sys.stdin.readline
inf=sys.maxsize

dx,dy=[0,0,-1,1],[-1,1,0,0]
cnt=0
while True:
    cnt+=1
    n=int(input())
    if n==0:
        break
    matrix=[list(map(int,input().split()))for i in range(n)]
    costbox=[[inf for i in range(n)]for j in range(n)]
    costbox[0][0]=matrix[0][0]
    queue=[(matrix[0][0],0,0)]
    while queue:
        cost,x,y=heappop(queue)
        if cost>costbox[y][x]:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<n:
                val=cost+matrix[ny][nx]
                if costbox[ny][nx]>val:
                    costbox[ny][nx]=val
                    heappush(queue,(val,nx,ny))
    print(f'Problem {cnt}:',costbox[-1][-1])
    
            
    

# 결승점만 보면 되는거 아닌가?

from collections import deque
from sys import stdin
input=stdin.readline

inf=float('inf')

dx=[0,0,1,-1]
dy=[1,-1,0,0]
n,m=map(int,input().split())
arr=[list(input().rstrip()) for i in range(n)]
vi=[[[inf]*m for i in range(n)] for j in range(2)]
queue=deque([])

for i in range(n):
    for j in range(m):
        if arr[i][j]=="N":
            vi[0][i][j]=0
            queue.append((0,j,i))
        elif arr[i][j]=="#":
            vi[0][i][j]=-1
        elif arr[i][j]=="G":
            vi[1][i][j]=0
            queue.append((1,j,i))
        elif arr[i][j]=="D":
            end=(j,i)
# 
while queue:
    typ,x,y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<m and -1<ny<n:
            if vi[typ][ny][nx]==inf:
                vi[typ][ny][nx]=vi[typ][y][x]+1
                queue.append((typ,nx,ny))

if vi[1][end[1]][end[0]]>=vi[0][end[1]][end[0]]:
    print("Yes")
else:
    print("No")

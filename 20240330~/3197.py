from sys import stdin
from collections import deque
input=stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def get_bfs(queue):
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if -1<nx<m and -1<ny<n:
                if depth[ny][nx]==0 and arr[ny][nx]=='X':
                    depth[ny][nx]=depth[y][x]+1
                    queue.append((nx,ny))

def check(day):
    vi=[[-1]*m for i in range(n)]
    for x,y in wheron:
        vi[y][x]=0
    
    queue=deque([wheron[0]])
    while queue:
        x,y=queue.popleft()
        if x==wheron[1][0] and y==wheron[1][1]:
            return True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<m and -1<ny<n:
                if vi[ny][nx]==0 and depth[ny][nx]<=day:
                    vi[ny][nx]=1
                    queue.append((nx,ny))
    return False

n,m=map(int,input().split())
arr=[input().rstrip() for i in range(n)]
wheron=[]
depth=[[0]*m for i in range(n)]
queue=deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j]=='X' and depth[i][j]==0:
            able=False
            for d in range(4):
                ni=i+dy[d]
                nj=j+dx[d]
                if -1<nj<m and -1<ni<n:
                    if arr[ni][nj]=='.':
                        able=True
                        break
            if able:
                depth[i][j]=1
                queue.append((j,i))
        elif arr[i][j]=='L':
            wheron.append((j,i))

get_bfs(queue)

mn=0
mx=1500*750

while mn<mx:
    mid=(mn+mx)//2
    if check(mid):
        mx=mid-1
    else:
        mn=mid+1

print(mn,mx)


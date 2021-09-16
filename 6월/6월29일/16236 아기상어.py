import sys
input=sys.stdin.readline
n=int(input())
sea=[list(map(int,input().split()))for i in range(n)]
visited=[[0 for i in range(n)]for j in range(n)]
dx,dy=[0,0,-1,1],[1,-1,0,0]
size,eat=2,0
timespend=0
beforemove=0
move=0

for i in range(n):
    for j in range(n):
        if sea[i][j]==9:
            sea[i][j]=0
            queue=[(0,1,i,j)]

while queue:
    if move<queue[0][0]:
        queue.sort()
    move,is_eat,y,x=queue.pop(0)
    if is_eat==0:
        sea[y][x]=0
        queue=[]
        visited=[[0 for i in range(n)]for j in range(n)]
        eat+=1
        if eat==size:
            size+=1
            eat=0
        timespend=move
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[ny][nx]==0:
                if 0<sea[ny][nx]<size:      
                    visited[ny][nx]=1
                    queue.append((move+1,0,ny,nx))
                elif sea[ny][nx]==0 or sea[ny][nx]==size:
                    visited[ny][nx]=1
                    queue.append((move+1,1,ny,nx))
                    
print(timespend)

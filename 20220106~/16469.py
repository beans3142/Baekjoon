from sys import stdin
from collections import deque
input=stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m=map(int,input().split())

matrix=[input().rstrip() for i in range(n)]

vi=[[[-1,-1,-1] for i in range(m)] for j in range(n)]

queue=deque([])
for i in range(3):
    y,x=map(int,input().split())
    vi[y-1][x-1][i]=0
    queue.append((x-1,y-1,i))

ans=0
gather=False
time=0

while queue:
    le=len(queue)
    for _ in range(le):
        x,y,typ=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<m and -1<ny<n:
                if vi[ny][nx][typ]==-1 and matrix[ny][nx]=='0':
                    vi[ny][nx][typ]=vi[y][x][typ]+1
                    queue.append((nx,ny,typ))
                    if vi[ny][nx][0]!=-1 and vi[ny][nx][1]!=-1 and vi[ny][nx][2]!=-1:
                        gather=True
                        ans+=1
    time+=1
    if gather:
        break

if ans:
    print(time)
    print(ans)
else:
    print(-1)

'''                       
for i in range(3):
    for j in range(n):
        for k in range(m):
            print(vi[j][k][i],end=' ')
        print()
    print()'''

from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
dx,dy=[1,-1,0,0],[0,0,-1,1]

before=[list(map(int,input().split())) for i in range(n)]
after=[list(map(int,input().split())) for i in range(n)]

vi=[[0 for i in range(m)]for i in range(n)]
group={}

def bfs(x,y,group_idx):
    global vi,group
    queue=deque([[x,y]])
    group[(x,y)]=group_idx
    vi[y][x]=1
    while queue:
        X,Y=queue.popleft()
        group[(X,Y)]=group_idx
        for i in range(4):
            nx=X+dx[i]
            ny=Y+dy[i]
            if -1<nx<m and -1<ny<n:
                if vi[ny][nx]==0 and before[ny][nx]==before[y][x]:
                    vi[ny][nx]=1
                    group[(nx,ny)]=group_idx
                    queue.append([nx,ny])

num=0
for I in range(m):
    for J in range(n):
        if vi[J][I]==0:
            bfs(I,J,num)
            num+=1
    
        
dif_c=None
dif_color=None
cnt=0
stop=False

for i in range(m):
    for j in range(n):
        if before[j][i]!=after[j][i]:
            if dif_c!=group[(i,j)]:
                dif_color=after[j][i]
                dif_c=group[(i,j)]
                cnt+=1
            if after[j][i]!=dif_color:
                if not stop:
                    print('NO')
                    stop=True
        if group[(i,j)]==dif_c:
            if before[j][i]==after[j][i]:
                if not stop:
                    print('NO')
                    stop=True
if not stop:
    if cnt<2:
        print('YES')
    else:
        print('NO')

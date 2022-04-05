from sys import stdin
from collections import deque
input=stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n=int(input())
matrix=[input().rstrip() for i in range(n)]
vi=[[0 for i in range(n)]for i in range(n)]
no=1
ans=[]

def bfs(X,Y,fill):
    cnt=1
    queue=deque([(X,Y)])
    vi[Y][X]=fill
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<n:
                if vi[ny][nx]==0 and matrix[ny][nx]!='0':
                    vi[ny][nx]=fill
                    cnt+=1
                    queue.append((nx,ny))
    return cnt

for i in range(n):
    for j in range(n):
        if matrix[i][j]=='1' and vi[i][j]==0:
            ans.append(bfs(j,i,no))
            no+=1

print(len(ans))
for i in sorted(ans):
    print(i)

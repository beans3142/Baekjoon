import sys
input=sys.stdin.readline
n=int(input())
matrix=[input().rstrip() for i in range(n)]
visited=[[False for i in range(n)]for i in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    global cnt
    cnt+=1
    visited[y][x]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<n and -1<ny<n:
            if matrix[ny][nx]=='1' and visited[ny][nx]==False:
                dfs(nx,ny)

line=[]

for i in range(n):
    for j in range(n):
        if visited[i][j]==False and matrix[i][j]=='1':
            cnt=0
            dfs(j,i)
            line.append(cnt)

print(len(line))
for i in sorted(line):
    print(i)

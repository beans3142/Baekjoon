from sys import stdin
input=stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y,bef,left,val):
    global ans
    ans=max(ans,val)
    if left==0:
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<m and -1<ny<n:
            if vi[ny][nx]==0:
                vi[ny][nx]=vi[y][x]+1
                if bef==i and left>0:
                    dfs(nx,ny,i,left-1,val+arr[ny][nx])
                elif left>1:
                    dfs(nx,ny,i,left-2,val+arr[ny][nx])
                vi[ny][nx]=0
                

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
vi=[[0]*m for i in range(n)]

sy,sx,p=map(int,input().split())
vi[sy][sx]=1
ans=arr[sy][sx]

if p>0:
    for i in range(4):
        x=sx+dx[i]
        y=sy+dy[i]
        if -1<x<m and -1<y<n:
            vi[y][x]=2
            dfs(x,y,i,p-1,arr[sy][sx]+arr[y][x])
            vi[y][x]=0

print(ans)

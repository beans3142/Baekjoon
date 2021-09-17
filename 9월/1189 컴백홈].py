from sys import stdin
input=stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]
r,c,k=map(int,input().split())
vi=[[0]*c for i in range(r)]
matrix=[input().rstrip() for i in range(r)]
cnt=0
vi[r-1][0]=1

def dfs(x,y,move):
    global cnt
    #print(x,y,move,k-move,c-1-x+y)
    if move==k and x==c-1 and y==0:
        cnt+=1
    if k-move<c-1-x+y or move>k:
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<c and -1<ny<r:
            if matrix[ny][nx]!='T':
                if vi[ny][nx]==0:
                    vi[ny][nx]=1
                    dfs(nx,ny,move+1)
                    vi[ny][nx]=0

dfs(0,r-1,1)

print(cnt)

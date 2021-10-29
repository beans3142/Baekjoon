from sys import stdin
input=stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y,vi):
    print(vi)
    if len(vi)==n//2:
        v[y][x]=1
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<ny<d and -1<nx<d:
            if matrixs[ny][nx]!=matrixe[ny][nx]:
                dfs(nx,ny,vi+[matrixs[ny][nx]])

def dfs2(x,y,vi):
    if len(vi)==(n+1)//2:
        if vi[y][x]==1:
            print('able')
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<ny<d and -1<nx<d:
            if matrixs[ny][nx]!=matrixe[ny][nx]:
                dfs(nx,ny,vi+[matrixs[ny][nx]])
    
        
while True:
    
    start,d,n=input().rstrip().split()
    d=int(d)
    n=int(n)
    matrixs=[]
    matrixe=[]
    v=[[0]*d for i in range(d)]
    for i in range(d):
        matrixs.append(input().rstrip().split())
    for i in range(d):
        matrixe.append(input().rstrip().split())
        
    for i in range(d):
        for j in range(d):
            if matrixs[i][j]=='X':
                start=j,i
            if matrixe[i][j]=='X':
                end=j,i

    dfs(start[0],start[1],[])
    dfs2(end[0],end[1],[])
    end=input().rstrip()

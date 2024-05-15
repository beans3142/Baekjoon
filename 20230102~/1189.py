r,c,k=map(int,input().split())
arr=[input() for i in range(r)]
ans=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]
vi=[[0]*c for i in range(r)]
def bt(x,y,d):
    global ans
    if d==k :
        if x==c-1 and y==0:
            ans+=1
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<c and -1<ny<r:
            if vi[ny][nx]==0 and arr[ny][nx]=='.':
                vi[ny][nx]=1
                bt(nx,ny,d+1)
                vi[ny][nx]=0
vi[r-1][0]=1
bt(0,r-1,1)
print(ans)

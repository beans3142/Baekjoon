from sys import stdin
input=stdin.readline

def getmin(x1,y1,x2,y2):
    v=1e9
    for i in range(x1,x2+1):
        v=min(v,arr[y1][i],arr[y2][i])
    for i in range(y1,y2+1):
        v=min(v,arr[i][x1],arr[i][x2])
    return v

def getcap(v,x1,y1,x2,y2):
    total=0
    for i in range(y1+1,y2):
        for j in range(x1+1,x2):
            if arr[i][j]>=v:
                return 0
            total+=v-arr[i][j]
    return total
            

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    arr=[list(map(int,input().split())) for i in range(n)]
    ans=0
    for i in range(n):
        for j in range(m):
            for ii in range(i+2,n):
                for jj in range(j+2,m):
                    v=getmin(j,i,jj,ii)
                    ans=max(ans,getcap(v,j,i,jj,ii))
    print(ans)

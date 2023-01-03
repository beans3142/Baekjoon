from sys import stdin
input=stdin.readline

def check():
    vi=[[0]*m for i in range(n)]
    total=0
    for i in range(n):
        for j in range(m):
            if vi[i][j]==0:
                if con[i][j]==0:
                    now=j
                    val=0
                    while now<m:
                        if con[i][now]!=0:
                            break
                        val=val*10+arr[i][now]
                        vi[i][now]=1
                        now+=1
                    total+=val
                else:
                    now=i
                    val=0
                    while now<n:
                        if con[now][j]!=1:
                            break
                        val=val*10+arr[now][j]
                        vi[now][j]=1
                        now+=1
                    total+=val
    return total
                

def mkcase(x,y,cnt):
    global ans
    if x==0 and y==n:
        ans=max(ans,check())
        return
    con[y][x]=1
    mkcase((x+1)%m,y+(x+1==m),cnt+1)
    con[y][x]=0
    mkcase((x+1)%m,y+(x+1==m),cnt+1)


n,m=map(int,input().split())
arr=[list(map(int,list(input().rstrip()))) for i in range(n)]
con=[[0]*m for i in range(n)]
ans=0
mkcase(0,0,0)
print(ans)
  

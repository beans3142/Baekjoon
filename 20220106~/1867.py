from sys import stdin
input=stdin.readline

def dfs(x):
    if vir[x]:
        return False
    vir[x]=True
    for nxt in case[x]:
        if rev[nxt]==-1 or dfs(rev[nxt]):
            rev[nxt]=x
            return True
    return False
        

n,k=map(int,input().split())
m=n
arr=[[1]*(m+1) for i in range(n+1)]
for i in range(k):
    x,y=map(int,input().split())
    arr[x][y]=0

cnt=0

rev=[-1]*(m+1)

case=[[] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i][j]==0:
            case[i].append(j)

for i in range(1,n+1):
    vir=[0]*(n+1)
    if dfs(i):
       cnt+=1 

print(cnt)

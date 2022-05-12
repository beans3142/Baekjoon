from sys import stdin
input=stdin.readline

def dfs(x):
    if vir[x]:
        return False
    vir[x]=True
    #vir[y]=True
    for nxt in case[x]:
        if rev[nxt]==-1 or dfs(rev[nxt]):
            rev[nxt]=x
            return True
    return False
        

r,c,n=map(int,input().split())
arr=[[1]*(r+1) for i in range(c+1)]
for i in range(n):
    a,b=map(int,input().split())
    arr[b][a]=0

cnt=0

rev=[-1]*(r+1)

case=[[] for i in range(c+1)]
for i in range(1,c+1):
    for j in range(1,r+1):
        if arr[i][j]:
            case[i].append(j)

for i in range(1,c+1):
    vir=[0]*(c+1)
    if dfs(i):
       cnt+=1 

print(cnt)

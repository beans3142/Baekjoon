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
        

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
row=[[0]*m for i in range(n)]
col=[[0]*m for i in range(n)]

cnt=1

rev=[-1]*(m+1)

case=[[] for i in range(n)]
for i in range(n):
    vi=[0]*(m)
    for j in range(m):
        if arr[i][j]!=2 and vi[j]==0:
            row[i][j]=cnt
            vi[j]=1
            j+=1
            while j<m:
                if arr[i][j]==2:
                    break
                row[i][j]=cnt
                vi[j]=1
                j+=1
            cnt+=1

case=[[] for i in range(cnt)]

cnt=1

for i in range(m):
    vi=[0]*n
    for j in range(n):
        if arr[j][i]!=2 and vi[j]==0:
            col[j][i]=cnt
            vi[j]=1
            j+=1
            while j<n:
                if arr[j][i]==2:
                    break
                col[j][i]=cnt
                vi[j]=1
                j+=1
            cnt+=1

rev=[-1]*cnt

for i in range(n):
    for j in range(m):
        if row[i][j]!=0 and arr[i][j]!=1:
            case[row[i][j]].append(col[i][j])

cnt=0

for i in range(len(case)):
    vir=[False]*(len(case))
    if dfs(i):
       cnt+=1 

print(cnt)

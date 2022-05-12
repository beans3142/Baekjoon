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
        

n=int(input())
arr=[input().rstrip() for i in range(n)]
row=[[0]*n for i in range(n)]
col=[[0]*n for i in range(n)]

cnt=1

rev=[-1]*(n+1)

case=[[] for i in range(n)]
for i in range(n):
    vi=[0]*(n)
    for j in range(n):
        if arr[i][j]=='.' and vi[j]==0:
            row[i][j]=cnt
            vi[j]=1
            j+=1
            while j<n:
                if arr[i][j]=='X':
                    break
                row[i][j]=cnt
                vi[j]=1
                j+=1
            cnt+=1

case=[[] for i in range(cnt)]

cnt=1

for i in range(n):
    vi=[0]*n
    for j in range(n):
        if arr[j][i]=='.' and vi[j]==0:
            col[j][i]=cnt
            vi[j]=1
            j+=1
            while j<n:
                if arr[j][i]=='X':
                    break
                col[j][i]=cnt
                vi[j]=1
                j+=1
            cnt+=1

rev=[-1]*cnt

for i in range(n):
    for j in range(n):
        if row[i][j]!=0:
            case[row[i][j]].append(col[i][j])

cnt=0

for i in range(len(case)):
    vir=[False]*(len(case))
    if dfs(i):
       cnt+=1 

print(cnt)

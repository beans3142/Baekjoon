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
arr=[[0]*n for i in range(n)]
row=[[0]*n for i in range(n*2-1)]
col=[[0]*n for i in range(n*2-1)]
k=int(input())
for i in range(k):
    x,y=map(int,input().split())
    arr[y-1][x-1]=1
    
narr=[[-1]*n for i in range(n*2-1)]
ndarr=[[-1]*n for i in range(n*2-1)]

for i in range(n):
    for j in range(i+1):
        narr[i][j]=arr[i-j][j]
        narr[~i][j]=arr[~(i-j)][~j]

ndarr=list(zip(*narr[::-1]))

cnt=1

for i in range(2*n-1):
    vi=[0]*n
    for j in range(n):
        if narr[i][j]==-1:
            break
        if narr[i][j]==0 and vi[j]==0:
            row[i][j]=cnt
            vi[j]=1
            j+=1
            while j<n:
                if narr[i][j]!=0:
                    break
                row[i][j]=cnt
                vi[j]=1
                j+=1
            cnt+=1

case=[[] for i in range(cnt)]

cnt=1

for i in range(2*n-1):
    vi=[0]*n
    for j in range(n):
        if ndarr[i][j]==-1:
            break
        if ndarr[i][j]==0 and vi[j]==0:
            col[i][j]=-cnt
            vi[j]=1
            j+=1
            while j<n:
                if ndarr[i][j]!=0:
                    break
                col[i][j]=-cnt
                vi[j]=1
                j+=1
            cnt+=1

rev=[-1]*cnt

for i in range(2*n-1):
    for j in range(n):
        if row[i][j]!=0:
            case[row[i][j]].append(col[i][j])

cnt=0

for i in range(len(case)):
    vir=[False]*(len(case))
    if dfs(i):
       cnt+=1 

print(cnt)

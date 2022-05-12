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
right=[[0]*n for i in range(n)]
left=[[9000]*n for i in range(n)]
k=int(input())
for i in range(k):
    x,y=map(int,input().split())
    arr[y-1][x-1]=1

cnt=1

y=n-1
x=n-1

for i in range(2*n-2,-1,-1):
    x=i
    y=0
    filled=False
    for j in range(i,-1,-1):
        try:
            if arr[y][x]!=1:
                right[y][x]=cnt
                filled=True
            else:
                cnt+=1
        except:
            pass
        x-=1
        y+=1

    cnt+=1

case=[[] for i in range(cnt)]

cnt=1

x=0
y=n-1
for i in range(2*n-2,-1,-1):
    nowx=x
    nowy=y
    for j in range(2*n+1):
        try:
            if arr[nowy][nowx]!=1:
                left[nowy][nowx]=min(left[nowy][nowx],cnt)
            else:
                cnt+=1
        except:
            pass
        nowx+=1
        nowy+=1
    y-=1
    cnt+=1

rev=[-1]*cnt

for i in range(n):
    for j in range(n):
        if right[i][j]!=0 and arr[i][j]!=1:
            case[right[i][j]].append(left[i][j])

cnt=0

for i in range(len(case)):
    vir=[False]*(len(case))
    if dfs(i):
       cnt+=1 

print(cnt)

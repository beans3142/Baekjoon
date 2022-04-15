from sys import stdin
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in people[x]:
        if work[i]==0 or dfs(work[i]):
            work[i]=x
            return True
    return False

n,m=map(int,input().split())
work=[0]*(1000+1)
people=[[] for i in range(1000+1)]
cnt=0
vi=[False]*(1000+1)

for i in range(n):
    info=map(int,input().split())
    for j in range(next(info)):
        people[i+1].append(next(info))

for i in range(1,n+1):
    for j in range(m+1):
        vi[j]=False
    if dfs(i):
        cnt+=1

print(cnt)

from sys import stdin
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in eat[x]:
        if rev[i]==-1 or dfs(rev[i]):
            rev[i]=x
            return True
    return False

def able(a1,b1,c1,a2,b2,c2,idx1,idx2):
    if a1==a2 and b1==b2 and c1==c2:
        if idx1<idx2:
            return True
        return False
    if a1>=a2 and b1>=b2 and c1>=c2:
        return True
    return False

n=int(input())
sharks=[list(map(int,input().split())) for i in range(n)]
eat=[[] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if able(*sharks[i],*sharks[j],i,j):
            eat[i].append(j)

cnt=0
rev=[-1]*n
for i in range(n):
    vi=[False]*(n+1)
    if dfs(i):
        cnt+=1
    vi=[False]*(n+1)
    if dfs(i):
        cnt+=1
    
print(rev.count(-1))

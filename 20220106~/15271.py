from sys import stdin
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in graph[x]:
        if rev[i]==-1 or dfs(rev[i]):
            rev[i]=x
            return True
    return False

n,m=map(int,input().split())

graph=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    if a%2!=b%2:
        graph[a].append(b)
        graph[b].append(a)

rev=[-1]*(n+1)
cnt=1

for i in range(1,n+1):
    vi=[False]*(n+1)
    cnt+=dfs(i)

if cnt>n:
    print(n)
else:
    print(cnt)

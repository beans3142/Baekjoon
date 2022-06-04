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

n,m,k1,k2=map(int,input().split())

graph=[[] for i in range(n+1)]

for i in range(k1):
    a,b=map(int,input().split())
    graph[a].append(b)

rev=[-1]*(m+1)
cnt=0

for i in range(1,n+1):
    vi=[False]*(n+1)
    cnt+=dfs(i)


graph=[[] for i in range(n+1)]

for i in range(k2):
    a,b=map(int,input().split())
    graph[a].append(b)

rev=[-1]*(m+1)
cnt2=0

for i in range(1,n+1):
    vi=[False]*(n+1)
    cnt2+=dfs(i)


if cnt>=cnt2:
    print("그만 알아보자")
else:
    print("네 다음 힐딱이")

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
types=['']*(n+1)
graph=[[] for i in range(n+1)]

for i in range(n):
    no,typ=input().rstrip().split()
    types[int(no)]=typ

for i in range(m):
    a,b=map(int,input().split())
    if types[a]=='c':
        graph[a].append(b)
    else:
        graph[b].append(a)

rev=[-1]*(n+1)
for i in range(1,n+1):
    vi=[0]*(n+1)
    dfs(i)

ans=rev.count(-1)-1
print(ans)

from sys import stdin
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=False
    for i in graph[x]:
        if rev[i]==-1 or dfs(rev[i]):
            rev[i]=x
            return True
    return False

def end():
    print(-1)
    exit()

n,m=map(int,input().split())

vi=[0]*(n+1)
mn=[0]*(n+1)
mx=[0]*(n+1)
val=[[0,0] for i in range(n+1)]

for i in range(m):
    typ,s,e,v=map(int,input().split())
    val[v][0]=max(val[v][0],l)
    for j in range(min(s,e),max(s,e)+1):
        if typ==1:
            if vi[v]:
                end()
            vi[v]=1
            mx[j]=v
        else:
            if vi[v]:
                end()
            vi[v]=1
            mn[j]=v

for i in range(1,n+1):
    if mx[i]<mn[i]:
        end()

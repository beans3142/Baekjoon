from sys import stdin
input=stdin.readline

def dfs(a):
    if vi[a]:
        return False
    vi[a]=True
    for b in graph[a]:
        if rev[b]==-1 or dfs(rev[b]):
            rev[b]=a
            return True
    return False

n,m=map(int,input().split())
    
graph=[[] for i in range(n+1)]
    
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
        
rev=[-1]*(n+1)
cnt=0
for i in range(1,n+1):
    vi=[False]*(n+1)
    if dfs(i):
        cnt+=1
            
print(n-cnt)



from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
v=[0]*(n+1)
able=True

def dfs(x,order):
    global v,able
    v[x]=order
        
    for i in graph[x]:
        if v[i]==order:
            able=False
        if v[i]==0:
            dfs(i,2 if order==1 else 1)
            

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1,1)

if able:
    print("Yes")
else:
    print("No")

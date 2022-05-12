def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if H[nx]==-1 or (not visited[H[nx]] and dfs(H[nx])):
            F[x]=nx
            H[nx]=x
            return 1
    return 0
def length(A,B):
    x1,y1=A;x2,y2=B
    return ((x1-x2)**2+(y1-y2)**2)**0.5
import sys
for lines in sys.stdin:
    n,m,s,v=map(int,lines.split())
    family=[[*map(float,input().split())] for _ in range(n)]
    house=[[*map(float,input().split())] for _ in range(m)]
    path=[[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if s*v>=length(family[i],house[j]):
                path[i].append(j)
    F=[-1]*n
    H=[-1]*m
    res=0
    for i in range(n):
        if F[i]==-1:
            visited=[0]*n
            if dfs(i):res+=1
    print(n-res)

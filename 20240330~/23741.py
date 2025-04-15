from sys import stdin,setrecursionlimit
from collections import deque
setrecursionlimit(100000)
input=stdin.readline

def dfs(now,curmov):
    nxtmov=curmov+1
    for nxt in graph[now]:
        if vi[nxtmov%2][nxt]==0:
            vi[nxtmov%2][nxt]=1
            dfs(nxt,nxtmov)

n,m,x,y=map(int,input().split())
graph=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

if not graph[x]:
    print(-1)
    exit()

vi=[[0]*(n+1) for i in range(2)]
vi[0][x]=1
dfs(x,0)
ans=[]
for i in range(1,n+1):
    if vi[y%2][i]==1:
        ans.append(i)
print(*ans)

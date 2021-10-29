from sys import stdin
from sys import setrecursionlimit
from collections import defaultdict as dd
from collections import deque as dq
input=stdin.readline
setrecursionlimit(10**6)

n,m=map(int,input().split())
v={i:{} for i in range(1,n+1)}
rv={i:{} for i in range(1,n+1)}

for i in range(m):
    a,b=map(int,input().split())
    v[b][a]=1
    rv[a][b]=1

def dfs(x):
    print(x)
    del v[x]
    for j in rv[x]:
        del v[j][x]
        if len(v[j])==0:
            dfs(j)

while v:
    for i in v:
        if len(v[i])==0:
            dfs(i)
            break

from sys import stdin
from math import gcd
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

for i in range(int(input())):
    n,m,k=map(int,input().split())
    graph=[[] for i in range(n+1)]
    for i in range(k):
        x,y=map(lambda x:int(float(x)),input().split())
        graph[x].append(y)

    rev=[-1]*202
    cnt=0
    for i in range(n):
        vi=[0]*(202)
        cnt+=dfs(i)
    print(cnt)
    

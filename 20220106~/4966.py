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

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    red=[]
    for i in range((n-1)//10+1):
        red+=list(map(int,input().split()))
    blue=[]
    for i in range((m-1)//10+1):
        blue+=list(map(int,input().split()))
    graph=[[] for i in range(n)]
    rev=[-1]*m
    for i in range(n):
        for j in range(m):
            if gcd(red[i],blue[j])!=1:
                graph[i].append(j)

    cnt=0
    for i in range(n):
        vi=[0]*n
        cnt+=dfs(i)
    print(cnt)
    

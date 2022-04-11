from sys import *
input=stdin.readline
setrecursionlimit(1000000)

n,q=map(int,input().split())
arr=[[i] for i in range(n+1)]
par=[i for i in range(n+1)]

def find(x):
    if x==par[x]:
        return x
    par[x]=find(par[x])
    return par[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if par[a]<par[b]:
        arr[a]+=arr[b]
        par[b]=par[a]
    elif par[b]<par[a]:
        arr[b]+=arr[a]
        par[a]=par[b]

for i in range(q):
    t=map(int,input().split())
    if next(t)==0:
        a,b=t
        union(a,b)
    else:
        k=next(t)
        find(k)
        print(len(arr[par[k]]))

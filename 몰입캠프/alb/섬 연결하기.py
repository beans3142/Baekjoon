from sys import *
setrecursionlimit(250000)
input=stdin.readline

n,m=map(int,input().split())
par=[i for i in range(n+1)]
arr=[]
minus=0

def find(x):
    if x==par[x]:
        return x
    par[x]=find(par[x])
    return par[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if par[a]<par[b]:
        par[b]=a
        return 0
    elif par[b]<par[a]:
        par[a]=b
        return 0
    else:
        return -1

for i in range(m):
    a,b=map(int,input().split())
    arr.append(sorted([a,b]))

for i in sorted(arr):
    a,b=i
    minus+=union(a,b)

print(len(set(par))-2-minus)

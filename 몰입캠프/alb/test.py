from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
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
        par[b]=par[a]
    elif par[b]<par[a]:
        par[a]=par[b]

for i in range(m):
    a,b=map(int,input().split())
    union(a,b)


print(len(set(par))-1)

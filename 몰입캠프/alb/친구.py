from sys import stdin
input=stdin.readline

n,q=map(int,input().split())

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
        par[b]=min(par[a],par[b])
        par[a]=min(par[a],par[b])
        par[b]=a
    else:
        par[b]=min(par[a],par[b])
        par[a]=min(par[a],par[b])
        par[a]=b

for i in range(q):
    t,a,b=map(int,input().split())
    if t==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
        

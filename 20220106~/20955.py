from sys import stdin
input=stdin.readline

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
        return 1

n,m=map(int,input().split())
tree=[[] for i in range(n+1)]
par=[i for i in range(n+1)]
ans=0

for i in range(m):
    u,v=map(int,input().split())
    ans+=union(u,v)


for i in range(1,n+1):
    find(i)

print(ans+len(set(par))-2)

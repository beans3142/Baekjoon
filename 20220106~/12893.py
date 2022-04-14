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
    elif par[a]>par[b]:
        par[a]=b

n,m=map(int,input().split())
par=[i for i in range(n+1)]
arr=[set() for i in range(n+1)]

for i in range(m):
    
    a,b=map(int,input().split())

    if arr[a]:
        union(min(arr[a]),par[b])
    if arr[b]:
        union(min(arr[b]),par[a])
        
    if find(a)==find(b):
        print(0)
        exit()
        
    arr[a].add(b)
    arr[b].add(a)
    

print(1)

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
    else:
        par[a]=b

n=int(input())
par=[i for i in range(n+1)]

for i in range(n-2):
    a,b=map(int,input().split())
    union(a,b)

for i in range(n):
    find(i+1)

for i in range(2,n+1):
    if find(par[i])!=find(par[i-1]):
        print(i,i-1)
        exit()

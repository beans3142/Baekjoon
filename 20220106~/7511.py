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

for _ in range(int(input())):
    n=int(input())
    k=int(input())
    par=[i for i in range(n)]

    for i in range(k):
        a,b=map(int,input().split())
        union(a,b)

    m=int(input())
    print(f"Scenario {_+1}:")
    for i in range(m):
        a,b=map(int,input().split())
        print(int(find(a)==find(b)))
    print()

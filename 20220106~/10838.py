from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
color=[0]*n
par=[0]*n

def lca(a,b):
    v=dict()
    if a==b:
        return a
    for i in range(1001):
        if a==0:
            break
        v[a]=1
        a=par[a]
    for i in range(1001):
        if b==0:
            break
        if b in v:
            return b
        b=par[b]
    return 0

def move(a,b):
    par[a]=b

def paint(a,b,c):
    end=lca(a,b)
    while a!=end:
        color[a]=c
        a=par[a]
    while b!=end:
        color[b]=c
        b=par[b]

def count(a,b):
    colors=set()
    end=lca(a,b)
    while a!=end:
        colors.add(color[a])
        a=par[a]
    while b!=end:
        colors.add(color[b])
        b=par[b]
    return len(colors)

for i in range(k):
    query=list(map(int,input().split()))
    if query[0]==1:
        paint(query[1],query[2],query[3])
    elif query[0]==2:
        move(query[1],query[2])
    else:
        print(count(query[1],query[2]))

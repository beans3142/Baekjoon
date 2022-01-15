from sys import stdin
input=stdin.readline

def find(tar):
    if tar==par[tar]:
        return tar
    par[tar]=find(par[tar])
    return par[tar]

def union(a,b):

    a=find(a)
    b=find(b)

    if a<b:
        par[b]=a
    else:
        par[a]=b

n,m=map(int,input().split())

par=list(range(n+1))

for i in range(m):
    do,a,b=map(int,input().split())
    if do==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')

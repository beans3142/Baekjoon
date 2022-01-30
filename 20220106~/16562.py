from sys import stdin
from collections import defaultdict
input=stdin.readline

def find(tar):
    if tar==par[tar]:
        return tar
    par[tar]=find(par[tar])
    return par[tar]

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        par[a]=b
    else:
        par[b]=a

n,m,k=map(int,input().split())
val=[0]+list(map(int,input().split()))
par=[1]+list(range(1,n+1))
group=defaultdict(list)
for i in range(m):
    v,w=map(int,input().split())
    union(v,w)

for i in range(1,n+1):
    find(i)

for i in range(1,n+1):
    group[par[i]].append(val[i])

mnmoney=0
for i in group:
    mnmoney+=min(group[i])

if mnmoney<=k:
    print(mnmoney)
else:
    print('Oh no')

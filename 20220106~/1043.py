from sys import stdin
from collections import defaultdict
from copy import deepcopy
input=stdin.readline

def find(tar):
    if tar==par[tar]:
        return tar
    par[tar]=find(par[tar])
    return par[tar]

def union(a,b):
    
    a=find(a)
    b=find(b)

    if par[a]<par[b]:
        Par[b]=min(Par[a],Par[b])
        Par[a]=min(Par[a],Par[b])
        par[b]=a
    else:
        Par[b]=min(Par[a],Par[b])
        Par[a]=min(Par[a],Par[b])
        par[a]=b


n,m=map(int,input().split())
Par=[1]*(n+1)
know=list(map(int,input().split()))
cnt=0
go=[]
par=list(range(n+1))
for i in range(know[0]):
    Par[know[i+1]]=0
for i in range(m):
    party=list(map(int,input().split()))
    go.append(party)
    for j in range(1,party[0]):
        union(party[j],party[j+1])

for i in range(1,n+1):
    find(i)

for party in go:
    able=True
    for i in range(party[0]):
        if Par[par[party[i+1]]]==0:
            able=False
            break
    cnt+=able
print(cnt)

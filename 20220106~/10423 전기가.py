from collections import deque
from heapq import heappop,heappush
from collections import defaultdict
from sys import stdin
input=stdin.readline

n,m,k=map(int,input().split())
gens=list(map(int,input().split()))
gen=[0]*(n+1)
for i in gens:
    gen[i]=1
    
# 유니온 파인드

def find(tar):
    if tar==par[tar]:
        return tar
    gen[tar]=max(par[gen[tar]],gen[tar])
    par[tar]=find(par[tar])
    return par[tar]

def union(a,b,val):
    global canremove
    c=a
    d=b
    a=find(a)
    b=find(b)

    if a<b and not gen[a]==gen[b]==1:
        par[b]=a
        gen[b]=gen[a]=max(gen[a],gen[b])
        mst[c][d]=mst[d][c]=val
    elif a>b and not gen[a]==gen[b]==1:
        par[a]=b
        gen[b]=gen[a]=max(gen[a],gen[b])
        mst[c][d]=mst[d][c]=val

mst={i:defaultdict(int) for i in range(1,n+1)}

par=list(range(n+1))

node=[]

for i in range(m):
    a,b,val=map(int,input().split())
    node.append((val,a,b))

node.sort()
    
for val,a,b in node:
    union(a,b,val)

total=0
for i in mst:
    for j in mst[i]:
        total+=mst[i][j]

print(total//2)

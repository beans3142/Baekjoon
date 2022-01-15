from collections import deque
from heapq import heappop,heappush
from collections import defaultdict

n,m=map(int,input().split())

# 유니온 파인드

def find(tar):
    if tar==par[tar]:
        return tar
    par[tar]=find(par[tar])
    return par[tar]

def union(a,b,val):
    global canremove
    c=a
    d=b
    a=find(a)
    b=find(b)

    if a<b:
        par[b]=a
        mst[c][d]=mst[d][c]=val
    elif a>b:
        par[a]=b
        mst[c][d]=mst[d][c]=val

mst={i:defaultdict(int) for i in range(1,n+1)}
canremove=0

par=list(range(n+1))

node=[]

for i in range(m):
    a,b,val=map(int,input().split())
    node.append((val,a,b))

node.sort()
    
for val,a,b in node:
    union(a,b,val)

mx=0
total=0
for i in mst:
    for j in mst[i]:
        mx=max(mst[i][j],mx)
        total+=mst[i][j]

print(total//2-mx)

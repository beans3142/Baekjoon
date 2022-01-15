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

# MST

mst={i:defaultdict(int) for i in range(1,n+1)}

# par의 개수는 노드 개수 ?

par=list(range(n+1))

# 가중치가 존재하는 간선 제작 

node=[]

for i in range(m):
    a,b,val=map(int,input().split())
    heappush(node,(val,a,b))

while node:
    val,a,b=heappop(node)
    union(a,b,val)


total=0
for i in mst:
    for j in mst[i]:
        total+=mst[i][j]

print(total//2)

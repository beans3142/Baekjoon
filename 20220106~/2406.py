from collections import deque
from heapq import heappop,heappush
from collections import defaultdict
from sys import stdin
input=stdin.readline

n,m=map(int,input().split())

# 유니온 파인드

def find(tar):
    if tar==par[tar]:
        return tar
    par[tar]=find(par[tar])
    return par[tar]

def union(a,b,val):
    global cnt
    c=a
    d=b
    a=find(a)
    b=find(b)

    if a<b:
        par[b]=a
        mst[c][d]=mst[d][c]=val
        cnt+=bool(val)
    elif a>b:
        par[a]=b
        mst[c][d]=mst[d][c]=val
        cnt+=bool(val)

mst={i:defaultdict(int) for i in range(1,n+1)}
cnt=0

par=list(range(n+1))

connected=[]

for i in range(m):
    a,b=map(int,input().split())
    connected.append((a,b))

matrix=[[0]*n]
line=list(map(int,input().split()))
for i in range(n-1):
    line=list(map(int,input().split()))
    line[0]=0
    matrix.append(line)

for a,b in connected:
    matrix[a-1][b-1]=matrix[b-1][a-1]=0

node=[]
for i in range(1,n):
    for j in range(i+1,n):
        node.append((matrix[i][j],i+1,j+1))

node.sort()

for val,a,b in node:
    union(a,b,val)

to_connect=[]
total=0
for i in mst:
    for j in mst[i]:
        total+=mst[i][j]
        if mst[i][j]!=0:
            to_connect.append((min(i,j),max(i,j)))

print(total//2,cnt)

if cnt>0:
    for a,b in set(to_connect):
        print(a,b)

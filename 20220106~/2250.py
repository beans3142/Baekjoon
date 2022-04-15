from sys import *
from collections import *
input=stdin.readline
setrecursionlimit(50000)

n=int(input())
tree=[[] for i in range(n+1)]
treex=defaultdict(int)
treey=defaultdict(list)
par=[0]*(n+1)
cnt=1
for i in range(n):
    node,left,right=map(int,input().split())
    tree[node].append(left)
    tree[node].append(right)
    if left!=-1:
        par[left]=node
    if right!=-1:
        par[right]=node
    
def dfs(x,depth):
    global cnt
    left=tree[x][0]
    right=tree[x][1]
    treey[depth].append(x)
    if left!=-1:
        dfs(left,depth+1)
    treex[x]=cnt
    cnt+=1
    if right!=-1:
        dfs(right,depth+1)

for i in range(1,n+1):
    if par[i]==0:
        dfs(i,1)
mxwi=0
mxidx=0

for idx in treey:
    i=treey[idx]
    wi=abs(treex[i[0]]-treex[i[-1]])+1
    if wi>mxwi:
        mxwi=wi
        mxidx=idx

print(mxidx,mxwi)

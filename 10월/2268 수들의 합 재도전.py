import sys
from math import ceil,log2
input=sys.stdin.readline

n,m=map(int,input().split())
size=2**ceil(log2(n))
tree=[0]*(size*2)

def init():
    for i in range(size-1,0,-1):
        tree[i]=tree[i*2]+tree[i*2+1]
        
def query(start,end,left,right,node):
    if right<start or end<left:
        return 0
    if left<=start and end<=right:
        return tree[node]
    mid=(start+end)//2
    return query(start,mid,left,right,node*2)+query(mid+1,end,left,right,node*2+1)

def update(index,diff):
    temp=index+size-1
    while temp>=1:
        tree[temp]+=diff
        temp//=2

for i in range(m):
    typ,N,M=map(int,input().split())
    if typ:
        update(N,M)
        print(tree)
    else:
        s,e=min(N,M),max(N,M)
        print(query(1,n+1,s,e,1))

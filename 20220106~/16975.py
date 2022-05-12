from sys import stdin
from math import ceil,log2
input=stdin.readline
def query(start,end,left,right,node,diff):
    if right<start or left>end:
        return
    if left<=start and end<=right:
        tree[node]+=diff
        return
    mid=(start+end)//2
    query(start,mid,left,right,2*node,diff)
    query(mid+1,end,left,right,2*node+1,diff)

def find(node):
    val=0
    while node>=1:
        val+=tree[node]
        node//=2
    return val

n=int(input())
size=2**ceil(log2(n))
tree=[0]*(2*size)
for i,j in enumerate(list(map(int,input().split()))):
    tree[size+i]=j
    
m=int(input())

for i in range(m):
    order=list(map(int,input().split()))
    if order[0]==1:
        query(1,size,order[1],order[2],1,order[3])
    else:
        val=find(size+order[1]-1)
        print(val)

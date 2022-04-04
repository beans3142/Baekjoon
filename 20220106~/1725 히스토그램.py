from math import *
from sys import stdin
input=stdin.readline

n=int(input())
arr=[0]*(n+2)
h_tree=2**(ceil(log2(n)+2))
tree=[0 for i in range(h_tree)]

def init(l,r,node):
    if l==r:
        tree[node]=(arr[l],arr[l],1 if arr[l]!=0 else 0)
        return
    else:
        mid=(l+r)//2
        init(l,mid,node*2)
        init(mid+1,r,node*2+1)
        a=tree[node*2]
        b=tree[node*2+1]
        mh=min(a[1] ,b[1])
        h=mh if mh!= 0 else max(a[1],b[1])
        tree[node]=(max(mh*(a[2]+b[2]),a[0],b[0])\
                                   ,h,a[2]+b[2])


for i in range(1,n+1):
    arr[i]=int(input())

init(1,n+1,1)

print(tree[1][0])

from math import *
from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
arr=[0]*(n+2)
h_tree=2**(ceil(log2(n)+1))
tree=[0 for i in range(h_tree)]

def init(l,r,node):
    if l==r:
        tree[node]=arr[l],(arr[l],arr[l])
        return
    else:
        mid=(l+r)//2
        init(l,mid,node*2)
        init(mid+1,r,node*2+1)
        a=tree[node*2]
        b=tree[node*2+1]
        tree[node]=(a[0]+b[0],\
                    (min(a[1][0] ,b[1][0])if min(a[1][0] ,b[1][0])!= 0 else max(a[1][1],b[1][1])\
                     ,max(a[1][1],b[1][1])))


def query(l,r,node,lidx,ridx):
    if ridx<l or r<lidx:
        return (10**10,0)
    elif lidx<=l and r<=ridx:
        return tree[node][1]
    mid=(l+r)//2
    a=query(l,mid,node*2,lidx,ridx)
    b=query(mid+1,r,node*2+1,lidx,ridx)
    return (min(a[0],b[0]),max(a[1],b[1]))

for i in range(1,n+1):
    arr[i]=int(input())

init(1,n+1,1)

for i in range(m):
    s,e=map(int,input().split())
    ans=query(1,n+1,1,s,e)
    print(ans[0])

from math import *
from sys import stdin
input=stdin.readline

n,q=map(int,input().split())
arr=[0]+list(map(int,input().split()))+[0]
h_tree=2**(ceil(log2(n)+1))
tree=[0 for i in range(h_tree)]

def init(l,r,node):
    if l==r:
        tree[node]=arr[l]
        return
    else:
        mid=(l+r)//2
        init(l,mid,node*2)
        init(mid+1,r,node*2+1)
        tree[node]=tree[node*2]+tree[node*2+1]

def update(l,r,node,idx,val):
    if l==r==idx:
        tree[node]=val
        return tree[node]
    if idx<l or r < idx:
        return 0
    else:
        mid=(l+r)//2
        update(l,mid,node*2,idx,val)
        update(mid+1,r,node*2+1,idx,val)
        tree[node]=tree[node*2]+tree[node*2+1]


def query(l,r,node,lidx,ridx):
    if ridx<l or r<lidx:
        return 0
    elif lidx<=l and r<=ridx:
        return tree[node]
    mid=(l+r)//2
    return query(l,mid,node*2,lidx,ridx) + query(mid+1,r,node*2+1,lidx,ridx)

init(1,n+1,1)

for i in range(q):
    a,b,N,M=map(int,input().split())
    s,e=min(a,b),max(a,b)
    print(query(1,n+1,1,s,e))
    update(1,n+1,1,N,M)

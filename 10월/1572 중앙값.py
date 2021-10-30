from math import *
from sys import stdin
from bisect import bisect_left
input=stdin.readline

n,k=map(int,input().split())
arr=[0]+list(map(int,input().split()))+[0]
h_tree=2**(ceil(log2(n)+1))
tree=[0 for i in range(h_tree)]

arr=[int(input()) for i in range(n)]

def init(l,r,node):
    if l==r:
        tree[node]=arr[l]
        return
    else:
        mid=(l+r)//2
        init(l,mid,node*2)
        init(mid+1,r,node*2+1)
        a=tree[node*2]
        b=tree[node*2+1]
        tree[node]=[a]+[b]

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
        tree[node]=min(tree[node*2],tree[node*2+1])

def query(l,r,node,lidx,ridx):
    if ridx<l or r<lidx:
        return 10**11
    elif lidx<=l and r<=ridx:
        return tree[node]
    mid=(l+r)//2
    a=query(l,mid,node*2,lidx,ridx)
    b=query(mid+1,r,node*2+1,lidx,ridx)
    return min(a,b)

m=int(input())
init(1,n+1,1)

from math import *
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
input=stdin.readline

n=int(input())
arr=[0]*n
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
        a=tree[node*2]
        b=tree[node*2+1]
        mh=min(a ,b)
        h=mh if mh!= -1 else max(a,b)
        tree[node]=h

def query(l,r,node,lidx,ridx):
    if ridx<l or r<lidx:
        return -1
    elif lidx<=l and r<=ridx:
        return tree[node]
    mid=(l+r)//2
    a=query(l,mid,node*2,lidx,ridx)
    b=query(mid+1,r,node*2+1,lidx,ridx)
    if a==-1:
        return b
    elif b==-1:
        return a
    elif arr[a]<arr[b]:
        return a
    return b

def biggest(Arr,l,r):
    Len=len(Arr)-1
    idx=query(1,n+1,1,l,r)
    print(idx)
    if r-l==0:
        return arr[idx]
    area=(r-l+1)*arr[idx]

    if l<idx:
        area=max(area,biggest(Arr,l,idx-1))
    if idx<r:
        area=max(area,biggest(Arr,idx+1,r))
    return area

for i in range(n):
    arr[i]=int(input())

init(1,n+1,1)
ans=biggest(arr,1,n+1)
print()

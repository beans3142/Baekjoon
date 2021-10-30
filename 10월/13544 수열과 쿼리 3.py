from math import *
from sys import stdin
from collections import deque
from bisect import bisect_right
from copy import deepcopy
input=stdin.readline

n=int(input())
arr=[[0]]+list(map(lambda x:[int(x)],input().split()))+[[]]
h_tree=2**(ceil(log2(n)+2))
tree=[[] for i in range(h_tree)]

def init(l,r,node):
    if l==r:
        tree[node]=arr[l]
        return tree[node]
    else:
        mid=(l+r)//2
        init(l,mid,node*2)
        init(mid+1,r,node*2+1)
        a=tree[node*2]
        b=tree[node*2+1]
        l=[0]*(len(a)+len(b))
        ai=0
        bi=0
        li=0
        while ai<len(a) and bi<len(b):
            if a[ai]<b[bi]:
                l[li]=a[ai]
                ai+=1
                li+=1
            else:
                l[li]=b[bi]
                bi+=1
                li+=1

        while ai<len(a):
            l[li]=a[ai]
            ai+=1
            li+=1
            
        while bi<len(b):
            l[li]=b[bi]
            bi+=1
            li+=1
            
        tree[node]=l

def query(l,r,node,lidx,ridx):
    if ridx<l or r<lidx:
        return 0
    elif lidx<=l and r<=ridx:
        return len(tree[node])-bisect_right(tree[node],k)
    mid=(l+r)//2
    a=query(l,mid,node*2,lidx,ridx)
    b=query(mid+1,r,node*2+1,lidx,ridx)
    on_l=a+b
    return on_l

init(1,n+1,1)
m=int(input())
las_ans=0
for i in range(m):
    s,e,k=map(int,input().split())
    s^=las_ans
    e^=las_ans
    k^=las_ans
    las_ans=query(1,n+1,1,s,e)
    print(las_ans)

from math import ceil,log2
from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(10**6)

def init(node,s,e):
    if s==e:
        tree[node]=arr[s],s
        return tree[node]

    mid=(s+e)//2
    fh=init(node*2,s,mid)
    sh=init(node*2+1,mid+1,e)
    tree[node]=min(fh,sh)
    return tree[node]

def minh(node,s,e,l,r):
    if l<=s and e<=r:
        return tree[node]
    elif e<l or r<s:
        return 10**11,-1
    mid=(s+e)//2
    fh=minh(node*2,s,mid,l,r)
    sh=minh(node*2+1,mid+1,e,l,r)
    return min(fh,sh)

def search(s,e):
    if e<s:
        return 0
    h,idx=minh(1,1,n,s,e)
    area=(e-s+1)*h
    return max(area,search(s,idx-1),search(idx+1,e))

n=int(input())
arr=[0]
for i in range(n):
    arr.append(int(input()))

height=size=2**(ceil(log2(n))+2)
tree=[0 for i in range(height)]
init(1,1,n)
print(search(1,n))

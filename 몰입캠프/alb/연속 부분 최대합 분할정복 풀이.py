from sys import stdin
from math import inf
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))

def dc(l,r):
    global ans
    if l==r:
        return arr[l]
    
    mid=(l+r)//2
    
    a=dc(l,mid)
    b=dc(mid+1,r)

    tmp=0
    lmax=-inf
    for i in range(mid,l-1,-1):
        tmp+=arr[i]
        lmax=max(lmax,tmp)

    tmp=0
    rmax=-inf
    for i in range(mid+1,r+1):
        tmp+=arr[i]
        rmax=max(rmax,tmp)
    
    return max(a,b,lmax+rmax)

print(dc(0,len(arr)-1))

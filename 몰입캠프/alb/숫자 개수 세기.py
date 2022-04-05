from collections import defaultdict

def ub(x):
    l=0
    r=n
    while l<r:
        mid=(l+r)//2
        if arr[mid]<=x:
            l=mid+1
        else:
            r=mid
    return r+1

def lb(x):
    l=0
    r=n
    while l<r:
        mid=(l+r)//2
        if arr[mid]<x:
            l=mid+1
        else:
            r=mid
    return r+1

n,q=map(int,input().split())
arr=sorted(map(int,input().split()))
query=map(int,input().split())

for i in query:
    print(ub(i)-lb(i))

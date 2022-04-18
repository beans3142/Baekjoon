from sys import stdin
from math import inf
input=stdin.readline

def lower(x):
    cnt=0
    for i in arr:
        cnt+=x//i if x//i<n else n
    return cnt

n=int(input())
k=int(input())
arr=[i for i in range(1,n+1)]
l=1
r=n**2
ans=inf
while l<=r:
    mid=(l+r)//2
    cnt=lower(mid)
    if cnt<k:
        l=mid+1
    else:
        r=mid-1
        ans=min(ans,mid)

print(ans)

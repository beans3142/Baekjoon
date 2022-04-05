from sys import stdin
from math import inf
input=stdin.readline

a=int(input())
l=1
r=a
ans=inf

while l<r:
    mid=(l+r)//2
    val=mid**2+mid
    if val<a:
        l=mid+1
    elif val==a:
        ans=mid
        break
    else:
        r=mid
        ans=mid-1

print(ans if ans!= inf else 0)

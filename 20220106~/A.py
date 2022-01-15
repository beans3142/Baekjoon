from itertools import permutations as per
from bisect import bisect_left

n,d=map(int,input().split())

def make_d(n,d):
    rev=[]
    while n:
        rev.append(n%d)
        n//=d
    return tuple(reversed(rev))

def make_n(arr):
    n=0
    for i in range(len(arr)):
        n+=arr[i]*d**(d-i-1)
    return n

able=True

nd=make_d(n+1,d)
if len(nd)<d:
    ans=list(range(d))
    ans[0],ans[1]=ans[1],ans[0]
elif len(nd)==d:
    case=list(per(range(d),d))
    idx=bisect_left(case,nd)
    if idx==len(case):
        able=False
    else:
        ans=case[idx]
else:
    able=False
if able:
    print(make_n(ans))
else:
    print(-1)

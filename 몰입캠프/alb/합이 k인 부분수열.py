from sys import stdin
from collections import defaultdict
from bisect import bisect_left
input=stdin.readline

n,k=map(int,input().split())
arr=list(map(int,input().split()))
dd=defaultdict(list)
presum=[0]*(n+1)
cnt=0

for i in range(1,n+1):
    presum[i]=presum[i-1]+arr[i-1]
    if presum[i]==k:
        cnt+=1
    dd[presum[i]].append(i)

for i in range(1,n+1):
    if dd[presum[i]-k]:
        cnt+=bisect_left(dd[presum[i]-k],i)

print(cnt)

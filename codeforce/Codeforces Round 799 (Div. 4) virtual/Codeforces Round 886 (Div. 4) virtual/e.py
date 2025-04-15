from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

def check(n):
    rmv=0
    for i in range(n+1):
        rmv=max(rmv,presum[i]+presum[-1]-presum[n-i])
    return rmv

for _ in range(int(input())):
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    presum=[0]
    for i in arr:
        presum.append(presum[-1]+i)
    if presum[-1]<s:
        print(-1)
        continue
    lo=0
    hi=n

    while lo<=hi:
        mid=(lo+hi)//2
        if presum[-1]-check(mid)<s:
            lo=mid+1
        else:
            hi=mid-1
    print(lo,hi,mid)



'''
12 3 
0 0 1 1 1 1 1 0 1 0 1 0
'''
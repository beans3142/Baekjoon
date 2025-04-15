from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

def check(h):
    s=0
    for i in arr:
        s+=max(h-i,0)
    return s


for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))

    lo=0
    hi=10**10

    while lo<=hi:
        mid=(lo+hi)//2
        if check(mid)<=k:
            lo=mid+1
        else:
            hi=mid-1
    print(hi)
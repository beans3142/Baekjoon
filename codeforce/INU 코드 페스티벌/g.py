from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

n, k = map(int, input().split())
arr = sorted(map(int, input().split()))

cnt=0

while arr and arr[-1]>=k:
    arr.pop()
    cnt+=1

l=0
r=len(arr)-1

while l<r:
    s=arr[l]+arr[r]
    if s<k:
        l+=1
    else:
        cnt+=1
        l+=1
        r-=1

print(cnt if cnt!=0 else -1)

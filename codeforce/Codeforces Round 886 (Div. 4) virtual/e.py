from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    n,c=map(int,input().split())
    arr=list(map(int,input().split()))
    low=0
    high=10**9
    while low<high:
        mid=(low+high)//2
        s=0
        for i in arr:
            s+=(i+2*mid)**2
        if s<c:
            low=mid+1
        elif s==c:
            break
        else:
            high=mid
    print(mid)
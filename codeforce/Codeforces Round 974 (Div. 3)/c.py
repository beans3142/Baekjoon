from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *
from itertools import combinations,permutations

def checkcase(add):
    val=(s+add)/(2*n)
    idx=bisect_left(arr,val)
    return idx
    

for _ in range(int(input())):
    n=int(input())
    arr=sorted(map(int,input().split()))
    mn=0
    mx=10**22
    s=sum(arr)
    rich=max(arr)

    while mn<=mx:
        mid=(mn+mx)//2
        arr[-1]+=mid
        loc=checkcase(mid)
        arr[-1]-=mid
        if loc>n//2:
            mx=mid-1
        else:
            mn=mid+1
    print(mn if mn != 10**22+1 else -1)

from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *
from itertools import combinations,permutations

for _ in range(int(input())):
    n,k=map(int,input().split())
    have=0
    arr=list(map(int,input().split()))
    ans=0
    for i in range(n):
        if arr[i]>=k:
            have+=arr[i]
        elif arr[i]==0:
            if have:
                have-=1
                ans+=1
    print(ans)
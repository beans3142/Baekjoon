from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=input().rstrip()
    cov=-1
    ans=0
    for i in range(n):
        if cov<i:
            if arr[i]=='B':
                cov=i+(k-1)
                ans+=1
    print(ans)
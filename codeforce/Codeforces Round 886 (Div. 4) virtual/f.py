from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    real=[0]*(n+1)
    for i in arr:
        if i<=n:
            real[i]+=1
    ans=[0]*(n+1)
    for i in range(1,n+1):
        if real[i]:
            for j in range(i,n+1,i):
                ans[j]+=real[i]

    print(max(ans))
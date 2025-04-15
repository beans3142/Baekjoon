from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *
from itertools import combinations,permutations

for _ in range(int(input())):
    n, d, k = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(k)]
    presum=[0]*(n+2)
    start=[0]*(n+2)
    end=[0]*(n+2)
    for i in arr:
        s,e=i
        presum[s]+=1
        presum[e+1]-=1
        start[s]+=1
        end[e]+=1
    
    for i in range(1,n+1):
        presum[i]+=presum[i-1]
    
    s=0

    for i in range(d):
        if start[1+i]==1:
            s+=1
    ansb=1
    ansm=1
    mn=s
    mx=s
    for i in range(1,n-d+1):
        if start[i+d]:
            s+=start[i+d]
        if end[i]:
            s-=end[i]
        if s<mn:
            ansm=i+1
            mn=s
        if mx<s:
            ansb=i+1
            mx=s
    print(ansb,ansm)

from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    n=int(input())
    ans=0
    mx=0
    for i in range(n):
        a,b=map(int,input().split())
        if a<=10:
            if mx<b:
                mx=b
                ans=i+1
    print(ans)
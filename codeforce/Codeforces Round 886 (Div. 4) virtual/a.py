from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if sum(sorted([a,b,c])[1:])>=10:
        print("YES")
    else:
        print("NO")
from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

ans=0

ay,ax=map(int,input().split())
by,bx=map(int,input().split())

if ax!=0 and ay!=0:
    ans=2
else:
    if bx==ax==0 and by<ay:
        ans=3
    elif by==ay==0 and bx<ax:
        ans=3
    else:
        ans=1
print(ans)
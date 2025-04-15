from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for i in range(int(input())):
    arr=[input().rstrip() for i in range(10)]
    case=[]
    for i in range(10):
        for j in range(10):
            if arr[i][j]=='X':
                case.append((i if i<5 else 9-i,j if j<5 else 9-j))
    ans=0
    for x,y in case:
        ans+=(1+min(x,y))
    print(ans)
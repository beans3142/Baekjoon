from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    n=int(input())
    arr=sorted(map(int,input().split()))
    arr[0]+=1
    ans=1
    for i in range(n):
        ans*=arr[i]
    print(ans)
from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

n,k=map(int,input().split())
arr=list(map(int,input().split()))

for i in range(k):
    left=set([i for i in range(i,n,k)])
    for j in range(i,n,k):
        if arr[j] not in left:
            print("No")
            exit()
        left.remove(arr[j])
print("Yes")

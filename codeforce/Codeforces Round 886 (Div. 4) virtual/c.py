from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    arr=[list(input().rstrip()) for i in range(8)]
    w=''
    for i in range(8):
        for j in range(8):
            if arr[i][j]!='.':
                w+=arr[i][j]
    print(w)
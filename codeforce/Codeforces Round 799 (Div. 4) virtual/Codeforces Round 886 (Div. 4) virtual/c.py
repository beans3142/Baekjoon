from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    cnt=0
    input()
    arr=[input().rstrip() for i in range(8)]
    for i in range(1,7):
        for j in range(1,7):
            if arr[i][j] == '#' and arr[i - 1][j - 1] == '#' and arr[i - 1][j + 1] == '#' and arr[i + 1][j - 1] == '#' and arr[i + 1][j + 1] == '#':
                print(i+1,j+1)


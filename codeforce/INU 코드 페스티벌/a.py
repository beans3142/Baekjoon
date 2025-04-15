from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

n, a, b = map(int, input().split())
po = 1
bo = 1 

for day in range(n):
    po += a
    bo += b

    if bo > po:
        po, bo = bo, po

    if po == bo:
        bo -= 1

print(po,bo)
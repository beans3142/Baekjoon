from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *
n, k = map(int, input().split())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    dist = sqrt(x ** 2 + y ** 2)
    points.append(dist)

points.sort()

def count(r, k):
    low = r
    high = r + k
    left = bisect_left(points, low)
    right = bisect_right(points, high)
    return right - left

max_points = 0

for r in points:
    cnt = count(r, k)
    max_points = max(max_points, cnt)

accuracy = (100 / n) * max_points
print(f"{accuracy:.6f}")

from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for i in range(int(input())):
    a,*left=map(int,input().split())
    print(sum([i>a for i in left]))
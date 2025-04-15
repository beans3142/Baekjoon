from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *
from itertools import combinations,permutations

for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%2:
        if k%4==3 or k%4==0:
            print("YES")
        else:
            print("NO")
    else:
        if k%4==1 or k%4==0:
            print("YES")
        else:
            print("NO")
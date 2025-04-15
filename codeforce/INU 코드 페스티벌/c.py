from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *


dx=[1,1,-1,-1,0,0,1,-1,0]
dy=[1,-1,1,-1,1,-1,0,0,0]

keyboard=[input().rstrip() for i in range(4)]

s=input().rstrip()

for i in range(1,3):
    for j in range(1,9):
        able=True
        left=list(s)
        for d in range(9):
            nx,ny=j+dx[d],i+dy[d]
            if keyboard[ny][nx] not in left:
                able=False
                break
            left.remove(keyboard[ny][nx])
        if able:
            print(keyboard[i][j])
            exit()

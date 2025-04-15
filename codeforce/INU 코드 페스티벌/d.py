from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

def match(x,y):
    for cx,cy,typ in loc:
        if cx==x and cy==y:
            return False
        if typ==1:
            if x<cx and y==cy:
                continue
            return False
        elif typ==2:
            if x<cx and cy<y:
                continue
            return False
        elif typ==3:
            if x==cx and cy<y:
                continue
            return False
        elif typ==4:
            if cx<x and cy<y:
                continue
            return False
        elif typ==5:
            if cx<x and y==cy:
                continue
            return False
        elif typ==6:
            if x>cx and cy>y:
                continue
            return False
        elif typ==7:
            if x==cx and y<cy:
                continue
            return False
        elif typ==8:
            if x<cx and y<cy:
                continue
            return False
    return True

n,m=map(int,input().split())
loc=[list(map(int,input().split())) for i in range(m)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if match(i,j):
            print(i,j)
from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

def getcnt(arr):
    cnt=0
    bef='s'
    c=0
    for i in arr:
        if bef!=i:
            cnt+=c*(c-1)
            bef=i
            c=1
        else:
            c+=1
    if c>1:
        cnt+=c*(c-1)
    return cnt


for _ in range(int(input())):
    n=int(input())
    ddx=[]
    ddy=[]
    ddd=[]
    ddr=[]
    ans=0

    for i in range(n):
        a,b=map(int,input().split())
        ddx.append(a)
        ddy.append(b)
        ddd.append(a-b)
        ddr.append(a+b)

    ddx.sort();ddr.sort();ddd.sort();ddy.sort()
    ans+=getcnt(ddx)
    ans+=getcnt(ddy)
    ans+=getcnt(ddd)
    ans+=getcnt(ddr)

    print(ans)

'''
1
5
0 0
2 2
-1 5
-1 10
2 11
'''
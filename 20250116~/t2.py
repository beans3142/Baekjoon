from sys import stdin,setrecursionlimit
input=stdin.readline
#setrecursionlimit(10000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *
from itertools import *
from decimal import *

dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,1,-1]

dd=defaultdict(int)
dq=deque()
hq=[]

def check(order,ns):
    cnt=0
    for i in order:
        co=1e19
        for j in range(3):
            if option[i][j]==0:
                continue
            co=min(co,ns[j]//option[i][j])
        for j in range(3):
            ns[j]-=co*option[i][j]
        cnt+=co
    return cnt

option=[(1,1,1),(2,0,1),(1,0,2)]

order=[(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]

n=int(input())
for a in range(10):
    for b in range(10):
        for c in range(10):
            for i in range(n):
                #a,b,c=map(int,input().split())
                ans=0
                for j in range(6):
                    ans=max(ans,check(order[j],[a,b,c]))

                #a, b, c = map(int, input().split())
                m = min(a, c)
                S = a + c
                b1 = min(b, m)
                y0 = max(0, 3 * m - S)   # 경계 y 값

                if b1 >= y0:
                    ans2 = m
                else:
                    ans2 = b1 + (S - 2 * b1) // 3

                if ans!=ans2:
                    print(a,b,c)


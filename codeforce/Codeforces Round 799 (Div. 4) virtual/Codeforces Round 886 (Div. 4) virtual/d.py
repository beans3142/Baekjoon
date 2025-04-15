from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    hour,term=input().split()
    h,m=map(int,hour.split(':'))
    term=int(term)
    t=h*60+m
    vi=set()
    div=24*60
    while t not in vi:
        vi.add(t)
        t+=term
        t%=div
    cnt=0
    for i in vi:
        rh=i//60
        if rh<9:
            rh=str(rh)+'0'
        else:
            rh=str(rh)[::-1]
        minu=str(i%60) if i%60>9 else '0'+str(i%60)
        if  minu==rh:
            cnt+=1
    print(cnt)
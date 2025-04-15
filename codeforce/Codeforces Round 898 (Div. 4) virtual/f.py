from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for i in range(int(input())):
    n,k=map(int,input().split())
    v=list(map(int,input().split()))
    h=list(map(int,input().split()))
    p1=0
    s=0
    cnt=0
    ans=0
    for p2 in range(n):
        if p2 and h[p2-1]%h[p2]:
            s=0
            p1=p2
        s+=v[p2]
        while k<s and p1<=p2:
            s-=v[p1]
            p1+=1
        ans=max(p2-p1+1,ans)

    print(ans)



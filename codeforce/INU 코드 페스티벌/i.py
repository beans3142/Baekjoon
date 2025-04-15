from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

def check(t):
    cnt=(t//a)+(t//b)+(t//c)
    return cnt

n, a,b,c=map(int,input().split())

s=1
e=10**25

while s<=e:
    mid=(s+e)//2
    if check(mid)>=n:
        e=mid-1
    else:
        s=mid+1
        

left=n-check(s-1)
lastdiv=[s%a==0,s%b==0,s%c==0]
ans=0
for i in range(3):
    if lastdiv[i]:
        left-=1
        if left==0:
            ans=i
if ans==0:
    print("A win")
elif ans==1:
    print("B win")
else:
    print("C win")
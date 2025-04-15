from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ei=1
    si=1
    now=arr[0]
    mul=1
    mx=1
    ans=arr[0]
    ansl=1
    ansr=1
    for i in range(1,n):
        if arr[i]==now:
            mul+=1
            ei+=1
            if mx<mul:
                mx=mul
                ans=arr[i]
                ansl=si
                ansr=ei
        else:
            mul-=1
            if mul==0:
                now=arr[i]
                mul=1
                si=i
                ei=i
    print(ans,ansl,ansr)
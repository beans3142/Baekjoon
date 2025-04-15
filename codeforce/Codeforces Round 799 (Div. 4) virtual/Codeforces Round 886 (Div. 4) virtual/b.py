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
    se=defaultdict(int)
    for i in arr:
        se[i]+=1
    cnt=[]
    for i in se:
        cnt.append(se[i])
    cnt.sort(reverse=True)
    if len(cnt)==1:
        print(cnt[0]%2)
        continue
    while cnt[0]>1:
        if cnt[0]>1 and cnt[1]>1:
            cnt[0]=cnt[0]-cnt[1]+1
            cnt[1]=1
        else:
            cnt[0]=cnt[0]%2
        cnt.sort(reverse=True)
    print(sum(cnt))
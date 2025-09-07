from sys import stdin,setrecursionlimit
input=stdin.readline
#setrecursionlimit(10000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *
from itertools import *
from decimal import *


n,k=map(int,input().split())
le=2**n
queue=deque([(1,le)])
left={1:2,2:0}
now=3
for i in range(n-1):
    qe=len(left)
    for j in range(1,qe+1):
        left[j],left[now]=now,left[j]
        now+=1

ans=[k//le for i in range(le)]

arr=[1]
nxt=1
for i in range(le-1):
    arr.append(left[nxt])
    nxt=left[nxt]
    
rev=[0]*(le+1)
for i in range(le):
    rev[arr[i]]=i

for i in range(1,k%le+1):
    ans[rev[i]]+=1
print(1 if k%le else 0)
print(*ans)

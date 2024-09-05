from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=sorted(map(int,input().split()))
    st=[arr[0]]
    group=[]
    for i in range(1,n):
        dif=abs(st[-1]-arr[i])
        if dif>k:
            group.append(len(st))
            st=[arr[i]]
        else:
            st.append(arr[i])
    if st:
        group.append(len(st))
    print(n-max(group))
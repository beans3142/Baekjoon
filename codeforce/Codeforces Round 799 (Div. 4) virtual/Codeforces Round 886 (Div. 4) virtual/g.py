from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    st=[arr[0]]
    ans=0
    for i in range(1,n):
        if arr[i-1]<arr[i]*2:
            st.append(arr[i])
            if len(st)>=k+1:
                ans+=1
        else:
            st=[arr[i]]
    print(ans)


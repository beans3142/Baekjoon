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
    digit=[0]*10
    touse=[]
    for i in arr:
        digit[i%10]+=1
        if digit[i%10]<3:
            touse.append(i%10)
    le=len(touse)
    able=False
    for i in range(le):
        for j in range(i+1,le):
            for k in range(j+1,le):
                if (touse[i]+touse[j]+touse[k])%10==3:
                    able=True
    if able:
        print("Yes")
    else:
        print("No")

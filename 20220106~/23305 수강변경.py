from sys import *
from collections import *
from bisect import *
from heapq import *
from math import *
dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,1,-1,1,-1,1,-1]
setrecursionlimit(10**6)
input=stdin.readline

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dd=defaultdict(int)
cnt=0

for i in range(n):
    dd[b[i]]+=1
for i in range(len(a)):
    if dd[a[i]]>0:
        n-=1
        dd[a[i]]-=1

print(n)

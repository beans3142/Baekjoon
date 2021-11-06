from sys import *
from collections import *
from bisect import *
from heapq import *
from math import *
dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,1,-1,1,-1,1,-1]
setrecursionlimit(10**6)
input=stdin.readline

n,m=map(int,input().split())
s=list(map(int,input().split()))
nums={i:1 for i in range(1,1001)}
ans=100000
for i in s:
    del nums[i]=0
nums=list(nums)
v=defaultdict(int)
for i in range(:
    for j in nums:
        v[i*j]=1

v=sorted(v)

for k in nums:
    for j in 

from sys import stdin
from heapq import heappush,heappop
from collections import deque
input=stdin.readline

n,k=map(int,input().split())

arr=sorted([list(map(int,input().split())) for i in range(n)])

ans=[]
for i in range(k):
    c=int(input())
    ans.append([c,[]])
ans=sorted(ans)

while arr:
    a=heappop(arr)
    if arr[0]

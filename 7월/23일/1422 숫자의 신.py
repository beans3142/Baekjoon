from heapq import heappush,heappop
from sys import stdin
input=stdin.readline
arr=[]

k,n=map(int,input().split())

for i in range(k):
    heappush(arr,int(input()))

n_arr=[]
left_arr=[]
for i in range(n):
    if arr:
        n_arr.append(heappop(arr))
    else:
        left_arr.append(arr[0])


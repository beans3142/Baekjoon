from sys import stdin
from bisect import bisect_left
input=stdin.readline

m=int(input())
left=0
arr=sorted(map(float,input().split()))
for i in range(1,m):
    n=i/m
    cnt=bisect_left(arr,n)
    print(cnt-left)
    left=cnt
print(len(arr)-cnt)

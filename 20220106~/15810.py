from sys import stdin
from bisect import *
input=stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

s=0
e=1000000**2

while s<e:
    cnt=0
    mid=(s+e)//2
    for i in range(n):
        cnt+=mid//arr[i]
    if cnt>=m:
        e=mid
    else:
        s=mid+1
    
print(s)

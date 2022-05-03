from sys import stdin
from collections import deque
input=stdin.readline

n,k=map(int,input().split())
arr=deque(map(int,input().split()))
s=0
karr=deque([])
for i in range(k):
    num=arr.popleft()
    karr.append(num)
    s+=num

ans=s

for i in range(k,n):
    s-=karr.popleft()
    num=arr.popleft()
    s+=num
    ans=max(ans,s)
    karr.append(num)
    
print(ans)

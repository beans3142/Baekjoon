from sys import stdin
from bisect import *

n=int(input())
arr=[0]+list(map(int,input().split()))
dp=[1]*(n+1)
mn={}
pd=[1]*(n+1)
nm={}
mx=0

for i in range(1,n+1):
    for j in mn:
        if mn[j]<arr[i]:
            dp[i]=max(dp[i],j+1)
    if dp[i] not in mn:
        mn[dp[i]]=arr[i]
    elif mn[dp[i]] > arr[i]:
        mn[dp[i]]=arr[i]

for i in range(n,0,-1):
    for j in nm:
        if nm[j]<arr[i]:
            pd[i]=max(pd[i],j+1)
    if pd[i] not in nm:
        nm[pd[i]]=arr[i]
    elif nm[pd[i]] > arr[i]:
        nm[pd[i]]=arr[i]

for i in range(n):
    mx=max(mx,dp[i]+pd[i]-1)

print(mx)

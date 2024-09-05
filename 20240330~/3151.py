from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))
dd=defaultdict(int)
for i in arr:
    dd[i]+=1
ans=0
for i in range(n):
    for j in range(i,n):
        if -(arr[i]+arr[j]) in dd:
            ans+=dd[-(arr[i]+arr[j])]
print(ans)

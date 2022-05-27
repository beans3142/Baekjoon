from sys import stdin
from collections import defaultdict
input=stdin.readline

n,k=map(int,input().split())
beforepresum=defaultdict(int)
arr=list(map(int,input().split()))
s=0 # 합
cnt=0

for i in range(n):
    s+=arr[i]
    if s==k:
        cnt+=1
    cnt+=beforepresum[s-k]
    beforepresum[s]+=1
    
print(cnt)

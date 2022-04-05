from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
l=0
r=n
arr=list(map(int,input().split()))
ans=0

def check(le):
    section=defaultdict(int)
    for i in range(le):
        section[arr[i]]+=1
    if len(section)==le:
        return True
    for i in range(le,n):
        front=i-le
        back=i
        section[arr[back]]+=1
        section[arr[front]]-=1
        if section[arr[front]]==0:
            del section[arr[front]]
        if len(section)==le:
            return True
    return False

while l<=r:
    mid=(l+r)//2
    able=check(mid)
    if able:
        l=mid+1
        ans=max(mid,ans)
    else:
        r=mid-1

print(ans)

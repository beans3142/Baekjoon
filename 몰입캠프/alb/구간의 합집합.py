from sys import stdin
from math import inf
input=stdin.readline

n=int(input())
section=sorted([list(map(int,input().split())) for i in range(n)])
k=int(input())+1
l=1
r=10**13 # 범위 조심.. 매우매우 커야함
ans=inf

def check(x):
    cnt=0
    for i in range(n):
        if section[i][0]>x:
            break
        if section[i][1]<=x:
            cnt+=section[i][1]-section[i][0]+1
        else:
            cnt+=x-section[i][0]+1
    return cnt

while l<r:
    mid=(l+r)//2
    cnt=check(mid)
    if cnt<k:
        l=mid+1
    else:
        r=mid
        ans=min(ans,mid)
    
print(ans)

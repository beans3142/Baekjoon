from math import lcm
from sys import stdin
input=stdin.readline
t=int(input())
for i in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    ans=nums[0]
    for j in range(1,n):
        lcm_=lcm(nums[j-1],nums[j])
        ans=max(ans,lcm_)
        nums[j]=lcm_
    print(ans%(10**9+7))

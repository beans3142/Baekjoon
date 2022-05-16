from sys import stdin
from math import factorial
input=stdin.readline

n=int(input())
dp=[0,1]
for i in range(2,n+1):
    dp.append((dp[-1]*i)%(10**9+7))

s=0
for i in range(1,n+1):
    s+=(n*(n+1)//2+i)*i
    s%=10**9+7

print(s,pow(dp[n],2,10**9+7))

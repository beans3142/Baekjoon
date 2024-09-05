from sys import stdin
input=stdin.readline

a,k=map(int,input().split())
dp=[1e9]*(1000001)

dp[a]=0
for i in range(a+1,k+1):
    dp[i]=min(dp[i-1],dp[i//2] if i%2==0 else 1e9)+1

print(dp[k])

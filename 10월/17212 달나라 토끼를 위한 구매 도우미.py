from sys import stdin,maxsize
input=stdin.readline

n=int(input())
inf=maxsize
dp=[inf]*(max(8,n+1))
dp[1]=dp[2]=dp[5]=dp[7]=1
dp[0]=0

for i in range(3,n+1):
    if dp[i]==inf:
        dp[i]=min(dp[i-7],dp[i-5],dp[i-2],dp[i-1])+1

print(dp[n])

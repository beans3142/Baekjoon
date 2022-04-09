from sys import stdin
input=stdin.readline

inf=float('inf')
n,k=map(int,input().split())
arr=list(map(int,input().split()))
dp=[0]*(n+1)
ans=-inf

for i in range(n):
    dp[i+1]=dp[i]+arr[i]
    
for i in range(k,n+1):
    ans=max(ans,dp[i]-dp[i-k])
    
print(ans)

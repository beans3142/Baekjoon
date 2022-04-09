from sys import stdin
input=stdin.readline

n=int(input())
arr=[input().rstrip() for i in range(n)]
dp=[[0 for i in range(n+1)] for i in range(3)]

for i in range(n):
    if arr[i]=='S':
        dp[0][i+1]=1
    elif arr[i]=='P':
        dp[1][i+1]=1
    elif arr[i]=='R':
        dp[2][i+1]=1
    for j in range(3):
        dp[j][i+1]=dp[j][i]+dp[j][i+1]

ans=0

for i in range(1,n):
    for j in range(3):
        for k in range(3):
            ans=max(ans,dp[j][i]+dp[k][n]-dp[k][i])


print(ans)

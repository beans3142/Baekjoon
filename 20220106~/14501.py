from sys import stdin
input=stdin.readline

n=int(input())
dp=[0]*(2001)
plan=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    dp[i]=max(dp[i],dp[i-1])
    dp[i+plan[i][0]]=max(dp[i+plan[i][0]],dp[i]+plan[i][1])

print(max(dp[:n+1]))

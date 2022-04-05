from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for i in range(n)]
dp=[[0 for i in range(m)] for i in range(n)]
dp[0][0]=matrix[0][0]

for i in range(1,n):
    dp[i][0]=matrix[i][0]+dp[i-1][0]

for i in range(1,m):
    dp[0][i]=matrix[0][i]+dp[0][i-1]

for i in range(1,n):
    for j in range(1,m):
        dp[i][j]=matrix[i][j]+max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])

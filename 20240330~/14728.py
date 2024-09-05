from sys import stdin
input=stdin.readline

n,t=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
dp=[[0]*(t+1) for i in range(n+1)]

# dp[i][j] = i개의 물건을 가져갔을때 무게가 w일때 얻을 수 있는 최대 value

for i in range(1,n+1):
    for j in range(1,t+1):
        if arr[i-1][0]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-arr[i-1][0]]+arr[i-1][1])

print(dp[-1][-1])
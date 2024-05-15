from sys import stdin
input=stdin.readline
ans=10e9
n=int(input())
rgb=[]
for i in range(n):
    rgb.append(list(map(int,input().split())))

dp=[[0]*3 for i in range(n+1)]

for j in range(3):
    for i in range(3):
        if i==j:
            dp[1][i]=rgb[1][i]
        else:
            dp[1][i]=10e9

    for i in range(2,n+1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2]

    for i in range(2):
        if i==j:
            continue
        ans=min(ans,dp[n][i])

print(ans)

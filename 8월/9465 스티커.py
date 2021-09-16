from sys import stdin

t=int(input())

for i in range(t):
    n=int(input())
    stickers=[list(map(int,input().split())) for i in range(2)]
    dp=[[0 for i in range(n)]for i in range(2)]
    for i in range(2):
        dp[i][0]=stickers[i][0]
    if n<2:
        print(max(dp[0][0],dp[1][0]))
        continue
    for i in range(2):
        dp[i][1]=stickers[i][1]+stickers[i-1][0]
    for j in range(2,n):
        for i in range(2):
            dp[i][j]=stickers[i][j]+max(dp[i-1][j-2],dp[i-1][j-1])
    print(max(max(dp[0]),max(dp[1])))

from sys import stdin
input=stdin.readline

inf = float('inf')

n,m=map(int,input().split())

dp=[[[inf,inf,inf] for i in range(m)] for j in range(n+1)]
arr=[list(map(int,input().split())) for i in range(n)]
dp[0]=[[0,0,0] for i in range(m)]

for i in range(1,n+1):
    for j in range(m):
        if j==0:
            dp[i][j][0]=arr[i-1][j]+min(dp[i-1][j+1][1],dp[i-1][j+1][2])
            
            dp[i][j][1]=dp[i-1][j][0]+arr[i-1][j]
            
        elif j==m-1:
            dp[i][j][2]=arr[i-1][j]+min(dp[i-1][j-1][1],dp[i-1][j-1][0])
            
            dp[i][j][1]=dp[i-1][j][2]+arr[i-1][j]
        else:
            dp[i][j][0]=arr[i-1][j]+min(dp[i-1][j+1][1],dp[i-1][j+1][2])

            dp[i][j][1]=arr[i-1][j]+min(dp[i-1][j][0],dp[i-1][j][2])

            dp[i][j][2]=arr[i-1][j]+min(dp[i-1][j-1][0],dp[i-1][j-1][1])
    


print(min([min(i) for i in dp[-1]]))

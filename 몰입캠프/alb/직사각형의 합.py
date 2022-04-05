from sys import stdin
input=stdin.readline

n,m,q=list(map(int,input().split()))
arr=[list(map(int,input().split())) for i in range(n)]
dp=[[0 for i in range(m+1)] for i in range(n+1)]

# 첫 줄 채워넣기
dp[0][0]=arr[0][0]
for i in range(1,n):
    #dp[0][i]=dp[0][i-1]+arr[0][i]
    dp[i][0]=dp[i-1][0]+arr[i][0]

for i in range(1,m):
    #dp[i][0]=dp[i-1][0]+arr[i][0]
    dp[0][i]=dp[0][i-1]+arr[0][i]

for j in range(1,n):
    for i in range(1,m):
        dp[j][i]=arr[j][i]+dp[j-1][i]+dp[j][i-1]-dp[j-1][i-1]

for i in range(q):
    a,b,c,d=map(int,input().split())
    a-=1
    b-=1
    print(dp[c][d]+dp[a][b]-dp[a][d]-dp[c][b])


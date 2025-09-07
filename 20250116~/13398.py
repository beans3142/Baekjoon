n=int(input())
arr=list(map(int,input().split()))
dp=[[-1111111111111111]*(n) for i in range(2)]
dp[0][0]=dp[1][0]=arr[0]
for i in range(n):
    dp[0][i]=max(arr[i],arr[i]+dp[0][i-1])
    dp[1][i]=max(dp[0][i-1],arr[i]+dp[1][i-1])
print(max(dp[0]+dp[1]))

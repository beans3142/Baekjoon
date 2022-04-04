import sys
input=sys.stdin.readline
#t=int(input())
for i in range(int(input())):
    n=int(input())
    dp=[0,1,1,1]+[0]*(n-3)
    for i in range(4,n+1):
        dp[i]=dp[i-2]+dp[i-3]
    print(dp[n])

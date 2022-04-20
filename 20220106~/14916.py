from sys import stdin
input=stdin.readline
inf=float('inf')
dp=[inf]*100001
dp[5]=1
dp[2]=1
dp[4]=2

for i in range(6,100001):
    dp[i]=1+min(dp[i-2],dp[i-5])


num=int(input())
print(dp[num] if dp[num]!=inf else -1)

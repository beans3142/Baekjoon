from sys import stdin
input=stdin.readline
n=int(input())
dp=[1,3,0]

for i in range(2,n+1):
    dp[2]=dp[1]*2+dp[0]
    

print(dp[n])

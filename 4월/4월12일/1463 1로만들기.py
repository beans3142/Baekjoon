import sys
n = int(sys.stdin.readline())
dp = [0]*1000001
dp[0] = 1000000
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4,n+1):
  a=0;b=0
  if n == 1:
      break
  if i%2 == 0:
    a = i//2
  if i%3 == 0:
    b = i//3
  dp[i] = min(dp[i-1]+1,dp[a]+1,dp[b]+1)
print(dp[n])

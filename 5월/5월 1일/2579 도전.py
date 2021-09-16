#https://www.acmicpc.net/problem/2579
#코드 출처 https://pacific-ocean.tistory.com/149
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])

'''
import sys

n=int(sys.stdin.readline())

dp=[0]+[0]*n

s=[0]+[int(sys.stdin.readline()) for i in range(n)]

dp[0]=s[0]
dp[1]=s[0]+s[1]
dp[2]=max(s[1]+s[2],s[0]+s[2])
for i in range(3,n):
    dp[i]=max(dp[i-3]+s[i-1]+s[i],dp[i-2]+s[i])
print(dp[n-1])
'''

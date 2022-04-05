# 1, 2, 3 을 이용하여 숫자 N을 만드는 경우의 수

# 더할 수 있는 최대의 수는 3
# n-1에 1을 붙여 n을 만들 수 있고,
# n-2에 2를 붙여 n을 만들 수 있고,
# n-3에 3을 붙여 n을 만들 수 있다.

from sys import stdin
input=stdin.readline
n=int(input())

dp=[0,1,2,4] # 맨 앞은 칸맞추기용, 각각 n=1,2,3일때 경우의 수

for i in range(3,n):
    dp.append((dp[-1]+dp[-2]+dp[-3])%1000007)

print(dp[n])

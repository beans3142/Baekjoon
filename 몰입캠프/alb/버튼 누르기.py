from sys import stdin
input=stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
dp=[[0 for i in range(3)]for i in range(n)]

dp[0]=arr[0]

for i in range(1,n):
    dp[i][0]=arr[i][0]+max(dp[i-1][1],dp[i-1][2])
    dp[i][1]=arr[i][1]+max(dp[i-1][0],dp[i-1][2])
    dp[i][2]=arr[i][2]+max(dp[i-1][0],dp[i-1][1])

print(max(dp[-1]))

'''
백준 단지번호 붙히기랑 같은 문제.
로직만 맞추면 문제없다.


'''

from sys import stdin
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))
try:
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=arr[0]+arr[1]
    dp[2]=max(arr[0]+arr[2],arr[1]+arr[2],dp[1])
    for i in range(3,n):
        dp[i]=max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i],dp[i-1])
except:
    pass
print(max(dp))

'''

초기 DP

dp[2] 설정 잘 하지 못한 경우
in
6
100 100 1 1 100 100

out
400
wa
301

in
1
100

out
100

in
2
100 100

out
200

'''

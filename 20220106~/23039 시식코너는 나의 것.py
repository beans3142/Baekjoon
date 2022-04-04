from sys import stdin
input=stdin.readline

n=int(input())

arr=[int(input()) for i in range(n)]
try:
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=max(dp[0]+arr[1]//2,arr[1])
    dp[2]=max(arr[0]+arr[2],arr[1]+arr[2]//2,arr[1])
    for i in range(3,n):
        dp[i]=max(dp[i-2]+arr[i],arr[i]//2+arr[i-1]+dp[i-3],dp[i-1])
except:
    pass
print(dp[-1])

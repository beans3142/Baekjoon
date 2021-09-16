# https://www.acmicpc.net/problem/1463

n=int(input())

dp=[0,0,1,1]+[0]*(n-3)
ndp={1:0,2:1,3:1}

for i in range(4,n+1):
    dp[i]=dp[i-1]+1
    ndp[i]=i-1
    if i%3==0:
        if dp[i]>dp[i//3]+1:
            dp[i]=dp[i//3]+1 # i//3 위치에서 *3 연산을 하겠다
            ndp[i]=i//3
    if i%2==0:
        if dp[i]>dp[i//2]+1:
            dp[i]=dp[i//2]+1 # i//2 위치에서 *2 연산을 하겠다
            ndp[i]=i//2

print(dp[n])
while ndp[n]:
    print(n,end=' ')
    n=ndp[n]
print(1)

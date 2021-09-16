n=int(input())

podoju=[]

for i in range(n):
    podoju.append(int(input()))

dp=[0]*n

if n<3:
    print(sum(podoju))
elif n==3:
    print(max(podoju[0]+podoju[1],podoju[1]+podoju[2]))
else:
    dp[0]=podoju[0]
    dp[1]=podoju[0]+podoju[1]
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+podoju[i],dp[i-3]+podoju[i-1]+podoju[i])
    print(dp[n-1])

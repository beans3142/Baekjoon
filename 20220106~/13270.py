from bisect import *

fibo=[0,1]

for i in range(1000):
    fibo.append(fibo[-1]+fibo[-2])
fibo[1]=0
n=int(input())
if n%2:
    mn=fibo[2]*(n//2-1)+fibo[3]
else:
    mn=fibo[2]*(n//2)

mx=0
dp=[0]*1000001
for i in range(2,30):
    dp[fibo[i]]=fibo[i-1]
    
for i in range(4,n+1):
    for j in range(2,1000):
        if i<fibo[j]:
            break
        dp[i]=max(dp[i],dp[i-fibo[j]]+dp[fibo[j]])

print(mn,dp[n])

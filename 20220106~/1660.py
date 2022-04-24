from bisect import *

n=int(input())

d2=[0,1]
d3=[0,1]


for i in range(2,140+1):
    d2.append(d2[-1]+i)
    d3.append(d3[-1]+d2[-1])

dp=[i for i in range(n+1)]

for i in range(1,n+1):
    for j in range(2,130):
        if i-d3[j]>=0:
            dp[i]=min(dp[i],dp[i-d3[j]]+1)
        else:
            break

print(dp[-1])

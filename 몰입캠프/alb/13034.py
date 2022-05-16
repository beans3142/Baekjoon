from collections import defaultdict
n=int(input())
dp=[0]*(n+1)
dp[2]=1
for i in range(3,n+1):
    able=defaultdict(int)

    for j in range((i-2)//2+1):
        able[dp[j]^dp[i-2-j]]=1

    for j in range(i+1):
        if able[j]==0:
            dp[i]=j
            break

if dp[-1]:
    print(1)
else:
    print(2)

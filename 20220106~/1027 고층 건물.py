n=int(input())
arr=[0]+list(map(int,input().split()))
arr2=[0]+list(reversed(arr[1:]))
dp=[1]*(n+1)
dp2=[1]*(n+1)
mn={}
mn2={}

for i in range(1,n+1):
    for j in mn:
        if mn[j]>arr[i]:
            dp[i]=max(dp[i],j+1)
    if dp[i] not in mn:
        mn[dp[i]]=arr[i]
    elif mn[dp[i]] < arr[i]:
        mn[dp[i]]=arr[i]

for i in range(1,n+1):
    for j in mn2:
        if mn2[j]>arr2[i]:
            dp2[i]=max(dp2[i],j+1)
    if dp2[i] not in mn2:
        mn2[dp2[i]]=arr2[i]
    elif mn2[dp2[i]] < arr2[i]:
        mn2[dp2[i]]=arr2[i]

ans=0
for i in range(1,n+1):
    ans=max(ans,dp[i]+dp2[i])

from sys import stdin
input=stdin.readline
n=int(input())
arr=[0]+list(map(int,input().split()))
dp=[1]*(n+1)
mn={}

for i in range(1,n+1):
	for j in mn:
		if mn[j]<arr[i]:
			dp[i]=max(dp[i],j+1)
	if dp[i] not in mn:
		mn[dp[i]]=arr[i]
	elif mn[dp[i]] > arr[i]:
		mn[dp[i]]=arr[i]

print(max(dp))

from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
presum=[0]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    presum[a-1]+=c
    presum[b]-=c
for i in range(1,n):
    presum[i]+=presum[i-1]
print(*(arr[i]+presum[i] for i in range(n)))

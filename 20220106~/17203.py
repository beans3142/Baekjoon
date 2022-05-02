from sys import stdin
input=stdin.readline

n,q=map(int,input().split())
arr=list(map(int,input().split()))
presum=[0,]
for i in range(1,len(arr)):
    presum.append(abs(arr[i]-arr[i-1]))

for i in range(1,len(presum)):
    presum[i]+=presum[i-1]

for i in range(q):
    a,b=map(int,input().split())
    print(presum[b-1]-presum[a-1])

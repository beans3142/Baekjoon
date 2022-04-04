from sys import stdin
input=stdin.readline

n,x=map(int,input().split())
arr=list(map(int,input().split()))
s1=0
for i in range(x):
    s1+=arr[i]

mx=s1
ans=1 if mx != 0 else 0

for i in range(x,n):
    s1=s1-arr[i-x]+arr[i]
    if s1>mx:
        mx=s1
        ans=1
    elif s1==mx:
        ans+=1

if mx!=0:
    print(mx)
    print(ans)
else:
    print('SAD')

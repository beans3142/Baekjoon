from sys import stdin
input=stdin.readline
n=int(input())
arr=sorted([int(input()) for i in range(n)],reverse=True)
ans=0
for i in range(n):
    if arr[i]-i<=0:
        break
    ans+=arr[i]-i    

print(ans)

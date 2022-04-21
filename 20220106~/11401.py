from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
ans=1
for i in range(n-k):
    ans=(ans*(n-i)//(i+1))

print(ans%1000000007)

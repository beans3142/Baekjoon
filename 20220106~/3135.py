from sys import stdin
input=stdin.readline
a,b=map(int,input().split())
n=int(input())
ans=abs(a-b)
for i in range(n):
    ans=min(ans,abs(int(input())-b)+1)

print(ans)

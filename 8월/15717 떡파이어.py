from sys import stdin
input=stdin.readline

n=int(input())-1
ans=1
mul=2

while n>0:
    if n&1==1:
        ans=ans*mul%(10**9+7)
    mul=mul*mul%(10**9+7)
    n>>=1

print(ans)


from sys import stdin
input=stdin.readline

n=int(input())
n1=0
n2=1
div=10**9+7
for i in range(2,n+1):
    n2,n1=(n1+n2)%div,n2

print(n2,n-2)

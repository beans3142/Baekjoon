from sys import stdin
input=stdin.readline

n=int(input())
biz=[int(input()) for i in range(n)]

total=sum(biz)
mx=max(biz)
if total-mx<=mx:
    print(2*mx-total)
else:
    print(total%2)

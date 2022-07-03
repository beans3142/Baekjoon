from sys import stdin
from math import gcd
input=stdin.readline

n=int(input())
arr=sorted(list(map(int,input().split())))
cnt=0

for i in range(1,n):
    if gcd(arr[i],arr[i-1])!=1:
        able=False
        for j in range(arr[i-1],arr[i]):
            if gcd(arr[i-1],j)==gcd(arr[i],j)==1:
                able=True
                break
        if able:
            cnt+=1
        else:
            cnt+=2

print(cnt)

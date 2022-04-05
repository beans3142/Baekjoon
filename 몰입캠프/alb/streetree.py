from sys import stdin
from collections import deque
from math import gcd
input=stdin.readline
n=int(input())
arr=sorted([int(input()) for i in range(n)])
difs=deque([])

for i in range(1,n):
    difs.append(arr[i]-arr[i-1])

while len(difs)>1:
    a=difs.popleft()
    b=difs.popleft()
    difs.append(gcd(a,b))


print((arr[-1]-arr[0])//difs[0]-len(arr)+1)

from sys import stdin
from math import factorial
from itertools import permutations
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))
per=list(permutations(arr,n))

ans=0
percent=[0]*100

for case in per:
    idx=0
    col=1
    cnt=0
    for j in case:
        for k in range(j):
            percent[idx]=col
            idx+=1
        col+=1

    for i in range(100):
        if percent[i-1]!=percent[i] and\
           percent[(i+50)%100]!=percent[(i+50)%100-1]:
            cnt+=1

    ans=max(cnt,ans)

print(ans//2)

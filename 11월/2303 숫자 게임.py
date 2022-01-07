from sys import stdin
from itertools import combinations,permutations
input=stdin.readline

n=int(input())

mx=0
ans=0
for i in range(n):
    nums=list(map(int,input().split()))
    cases=list(permutations(nums,3))
    casemx=0
    for case in cases:
        s=sum(case)%10
        if s>casemx:
            casemx=s
    if mx<=casemx:
        ans=i+1
        mx=casemx

print(ans)

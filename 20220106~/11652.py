from sys import stdin
from collections import Counter
input=stdin.readline

n=int(input())
arr=[int(input()) for i in range(n)]
print(sorted([(-j,i) for i,j in Counter(arr).items()])[0][1])

from sys import stdin
from math import ceil
input=stdin.readline

n=int(input())
files=list(map(int,input().split()))
size=int(input())
need=0

for i in range(n):
    need+=size*ceil(files[i]/size)
print(need)

from sys import stdin
from bisect import *
input=stdin.readline

n,k=map(int,input().split())
arr=[[] for i in range(4)]
for i in range(4):
    arr[i]=list(map(int,input().split()))

s1=set()
for i in range(n):
    for j in range(n):
        s1.add(arr[0][i]+arr[1][j])
a1=sorted(s1)

s2=set()
for i in range(n):
    for j in range(n):
        s2.add(arr[2][i]+arr[3][j])
a2=sorted(s2)


dif=float('inf')
ans=0

for i in s1:
    idx=bisect(a2,k-i)
    if idx==len(a2):
        idx-=1
    if dif>abs(k-(a2[idx]+i)):
        dif=abs(k-(a2[idx]+i))
        ans=a2[idx]+i

print(ans)

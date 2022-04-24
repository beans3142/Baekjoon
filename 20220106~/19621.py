from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
arr=sorted([list(map(int,input().split())) for i in range(n)])
dd=defaultdict(int)
for i in range(n):
    dd[arr[i][1]]=max(dd[arr[i][1]],arr[i][2])
    for j in dd:
        if j<=arr[i][0]:
            dd[arr[i][1]]=max(dd[arr[i][1]],dd[j]+arr[i][2])
    
mx=0
for i in dd:
    mx=max(dd[i],mx)

print(mx)

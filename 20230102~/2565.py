from sys import stdin
from bisect import bisect_left

n=int(input())
inp=[list(map(int,input().split())) for i in range(n)]
arr=[]
inp.sort()
for a,b in inp:
    arr.append(b)
ans=[]

for i in range(n):
    if not ans:
        ans.append(arr[i])
    if ans[-1]<arr[i]:
        ans.append(arr[i])
    else:
        loc=bisect_left(ans,arr[i])
        ans[loc]=arr[i]

print(n-len(ans))

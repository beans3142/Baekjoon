from sys import stdin
from bisect import bisect_left
input=stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(input()) for i in range(n)]
    ans=[arr[0]]
    for i in range(1,n):
        if ans[-1]<arr[i]:
            ans.append(arr[i])
        else:
            loc=bisect_left(ans,arr[i])
            ans[loc]=arr[i]
    print(len(ans))

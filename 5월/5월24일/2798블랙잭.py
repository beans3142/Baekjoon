import sys
input=sys.stdin.readline
n,m=map(int,input().split())

arr=list(map(int,input().split()))
mx=1

for i in range(n-2):
    for j in range(i+1,n-1):
        for p in range(j+1,n):
            if arr[i]+arr[j]+arr[p]<=m:
                mx=max(mx,arr[i]+arr[j]+arr[p])

print(mx)

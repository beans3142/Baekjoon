from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
arr=[input().rstrip() for i in range(n)]
mx=1
for i in range(n):
    for j in range(m):
        for k in range(min(m-j,n-i)):
            if arr[i][j]==arr[i+k][j]==arr[i][j+k]==arr[i+k][j+k]:
                mx=max(mx,k+1)
print(mx**2)

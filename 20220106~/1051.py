from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
arr=[input().rstrip() for i in range(n)]
mxlen=1

for i in range(n):
    for j in range(m):
        for k in range(i+1,n):
            dist=k-i+1
            if n-k<mxlen:
                break
            if j+dist>m:
                break
            if arr[i][j]==arr[k][j] and dist>mxlen:
                if arr[i][j+dist-1]==arr[k][j+dist-1]==arr[k][j]:
                    mxlen=dist

print(mxlen**2)

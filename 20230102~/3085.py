from sys import stdin
input=stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]
n=int(input())
ans=0
arr=[list(input().rstrip()) for i in range(n)]
def bf():
    mx=0
    garo=[[1]*n for i in range(n)]
    sero=[[1]*n for i in range(n)]
    for i in range(n):
        for j in range(1,n):
            if arr[i][j]==arr[i][j-1]:
                garo[i][j]=garo[i][j-1]+1
    for i in range(n):
        for j in range(1,n):
            if arr[j][i]==arr[j-1][i]:
                sero[j][i]=sero[j-1][i]+1
    for i in range(n):
        for j in range(n):
            mx=max(mx,garo[i][j],sero[i][j])
    return mx
for i in range(n):
    for j in range(n):
        for d in range(4):
            ni=i+dy[d]
            nj=j+dx[d]
            if -1<nj<n and -1<ni<n:
                arr[i][j],arr[ni][nj]=arr[ni][nj],arr[i][j]
                ans=max(ans,bf())
                arr[i][j],arr[ni][nj]=arr[ni][nj],arr[i][j]
print(ans)

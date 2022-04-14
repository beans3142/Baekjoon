from sys import stdin
input=stdin.readline

n=int(input())

arr=[list(map(int,input().split())) for i in range(n)]
ans=[0]*(n)
ans[0]=(arr[0][1]+arr[0][2]-arr[1][2])//2
for i in range(1,n):
    ans[i]=arr[0][i]-ans[0]

print(*ans)


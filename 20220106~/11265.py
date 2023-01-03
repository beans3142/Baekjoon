from sys import stdin
input=stdin.readline

n,m=map(int,input().split())

arr=[list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            arr[j][k]=min(arr[j][k],arr[j][i]+arr[i][k])

for i in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    if arr[a][b]<=c:
        print('Enjoy other party')
    else:
        print('Stay here')

from sys import stdin
input=stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    arr=sorted([list(map(int,input().split())) for i in range(n)])
    mx2=1e9
    cnt=0
    for i in range(n):
        if arr[i][1]<mx2:
            mx2=arr[i][1]
            cnt+=1
    print(cnt)

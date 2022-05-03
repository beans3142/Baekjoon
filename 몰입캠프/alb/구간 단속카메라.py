from sys import stdin
input=stdin.readline

n,s=map(int,input().split())
arr=[[0,0]]+[list(map(int,input().split())) for i in range(n)]
cnt=0

for i in range(1,n+1):
    speed=abs((arr[i-1][0]-arr[i][0])//(arr[i-1][1]-arr[i][1]))
    if speed>s:
        cnt+=1

print(cnt)

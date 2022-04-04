from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
arr=sorted([int(input()) for i in range(m)])
ans=(0,0)
for i in range(m):
    ans=max(ans,(arr[i]*min(m-i,n),arr[i]))

print(ans[1],ans[0])

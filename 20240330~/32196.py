from sys import stdin
input=stdin.readline

n,m,k,x,y=map(int,input().split())
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append(a*x-b*y)
arr.sort()
ans=k*(x+y)
for i in range(m):
    ans+=arr[i]
print(ans)

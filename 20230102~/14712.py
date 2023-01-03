from sys import stdin
input=stdin.readline

def check(x,y):
    global ans
    if x==0 and y==n:
        ans+=1
        return
    arr[y][x]=1
    if not arr[y-1][x-1]==arr[y-1][x]==arr[y][x-1]==arr[y][x]==1:
        check((x+1)%m,y+(x+1==m))
    arr[y][x]=0
    check((x+1)%m,y+(x+1==m))

n,m=map(int,input().split())

if n==1 or m==1:
    print(2**(n*m))
else:
    ans=0
    arr=[[0]*m for i in range(n)]
    check(0,0)
    print(ans)

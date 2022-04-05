n=int(input())
arr=[[0 for i in range(n)] for i in range(n)]
x,y,r=map(int,input().split())
x-=1
y-=1
arr[x][y]='x'
for i in range(1,r+1):
    for j in range(i+1):
        if -1<x+i-j<n and -1<y+j<n:
            arr[x+i-j][y+j]=i
        if -1<x-i+j<n and -1<y-j<n:
            arr[x-i+j][y-j]=i
        if -1<x+i-j<n and -1<y-j<n:
            arr[x+i-j][y-j]=i
        if -1<x-i+j<n and -1<y+j<n:
            arr[x-i+j][y+j]=i

for i in arr:
    print(*i)

from sys import stdin
input=stdin.readline

n,x=map(int,input().split())
arr=sorted(map(int,input().split()))
cnt=0
while arr and arr[-1]>=x:
    arr.pop()
    cnt+=1

l=0
r=len(arr)-1
left=len(arr)

while l<r:
    s=arr[l]+arr[r]
    if s+x/2>=x:
        cnt+=1
        r-=1
        l+=1
        left-=2
    else:
        l+=1

if left>=3:
    cnt+=left//3

print(cnt)

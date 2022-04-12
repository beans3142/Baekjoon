from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
arr=sorted(map(int,input().split()))
if n==1:
    print(0)
    exit()
l,r=0,n-1
s=arr[0]+arr[-1]
cnt=0
while True:
    if s==k:
        cnt+=1
    if s<=k:
        s-=arr[l]
        l+=1
        if l==r:
            break
        s+=arr[l]
    elif r<=l:
        break
    else:
        s-=arr[r]
        r-=1
        if l==r:
            break
        s+=arr[r]

print(cnt)

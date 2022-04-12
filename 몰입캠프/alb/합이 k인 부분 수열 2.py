from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
arr=sorted(map(int,input().split()))
l=r=0
s=0
cnt=0
while True:
    if k==s and r-l==2:
        print(l,r)
        cnt+=1
    if s>=k:
        s-=arr[l]
        l+=1
    elif r==n:
        break
    else:
        s+=arr[r]
        r+=1

print(cnt)

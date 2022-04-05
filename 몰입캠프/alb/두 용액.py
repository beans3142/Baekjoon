from sys import stdin
input=stdin.readline

def lb(l,r,x):
    while l<r:
        mid=(l+r)//2
        if arr[mid]<=x:
            l=mid+1
        else:
            r=mid-1
    return mid+1,mid,mid-1

n=int(input())
arr=sorted(map(int,input().split()))+[10**11]
mndif=10**11
ans=(0,0)
for i in range(n-1):
    first=arr[i]
    idxs=lb(i+1,n,-first)
    for idx in idxs:
        if idx==i:
            continue
        dif=abs(arr[idx]+first)
        if mndif>dif:
            mndif=dif
            ans=first,arr[idx]

print(*ans)

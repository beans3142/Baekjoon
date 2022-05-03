n=int(input())
arr=sorted(map(int,input().split()))
s=sum(arr)
if s//2<arr[-1]:
    ans=2*arr[-1]-s
elif s-arr[-1]==arr[-1]:
    ans=0
else:
    mx=arr[-1]
    s-=arr[-1]
    idx=0
    dif=s-mx
    while dif>arr[idx]*2:
        arr[idx+1]-=arr[idx]
        arr[idx]=0
        idx+=1
    arr[idx]-=dif//2
    arr[idx+1]-=dif//2
    ans=sum(arr)-2*arr[-1]

print(ans)

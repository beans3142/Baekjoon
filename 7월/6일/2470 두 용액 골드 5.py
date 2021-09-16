from sys import stdin
input=stdin.readline
n=int(input())
arr=list(map(int,input().split()))
l=0
r=n-1
mn=(2*10**10+1,0,0)
arr.sort()
while l<r:
    now=(abs(arr[l]+arr[r]),arr[l],arr[r])
    mn=min(now,mn)
    if abs(arr[l+1]+arr[r])<now[0]:
        l+=1
    elif abs(arr[l]+arr[r-1])<now[0]:
        r-=1
    else:
        l+=1
        r-=1
        
print(mn[1],mn[2])

def merge(arr):
    if len(arr)<=2:
        return sorted(arr)
    mid=len(arr)//2
    arr1=merge(arr[:mid])
    arr2=merge(arr[mid:])

    print(arr)

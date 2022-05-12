import sys ; input=sys.stdin.readline
n=int(input())
inf=float('inf')
arr=[]
for i in range(n):
    arr.append((int(input()),i))
ans=[inf]*n
swap=0

def mergesort(l,r):
    if l==r:
        ans[arr[l][1]]=min(ans[arr[l][1]],r+1)
        return [arr[l]]
    mid=(l+r)//2
    left=mergesort(l,mid)
    right=mergesort(mid+1,r)
    narr=[]
    left_idx=0
    right_idx=0
    while left_idx<len(left) and right_idx<len(right):
        if left[left_idx]>right[right_idx]:
            narr.append(left[left_idx])
            left_idx+=1
        else:
            narr.append(right[right_idx])
            right_idx+=1
    while left_idx<len(left):
        narr.append(left[left_idx])
        left_idx+=1
    while right_idx<len(right):
        narr.append(right[right_idx])
        right_idx+=1
    for i in range(len(narr)):
        ans[narr[i][1]]=min(ans[narr[i][1]],l+i+1)
    return narr

narr=mergesort(0,len(arr)-1)

print(*narr)

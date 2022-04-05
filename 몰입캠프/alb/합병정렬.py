n=int(input())
arr=list(map(int,input().split()))
def mergesort(l,r):
    print(l,r)
    if l==r:
        return [arr[l]]
    mid=(l+r)//2
    left=mergesort(l,mid)
    right=mergesort(mid+1,r)
    narr=[]
    left_idx=0
    right_idx=0
    while left_idx<len(left) and right_idx<len(right):
        if left[left_idx]<right[right_idx]:
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
    return narr

narr=mergesort(0,len(arr)-1)

print(*narr)

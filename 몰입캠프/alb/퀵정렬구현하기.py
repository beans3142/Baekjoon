
def getLR(s,e,pivot):
    left=[]
    right=[]
    for i in range(s,e+1):
        if arr[i]<=pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return left,right

def quicksort(l,r):
    global arr
    if l>=r:
        return;

    pivot=arr[l]
    left,right=getLR(l+1,r,pivot)

    for i in range(len(left)):
        arr[l+i]=left[i]
        
    arr[l+len(left)]=pivot
    
    for i in range(len(right)):
        arr[l+len(left)+1+i]=right[i]
        
    quicksort(l,l+len(left)-1)
    quicksort(l+len(left)+1,r)
        


n=int(input())
arr=list(map(int,input().split()))

quicksort(0,n-1)

print(*arr)

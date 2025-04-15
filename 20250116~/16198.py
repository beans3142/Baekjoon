n=int(input())
arr=list(map(int,input().split()))
def bt(n,s,arr):
    ans=0
    if n==2:
        return s
    for i in range(1,n-1):
        left=arr[:i]
        right=arr[i+1:]
        ans=max(ans,bt(n-1,s+left[-1]*right[0],left+right))
    return ans

print(bt(n,0,arr))
n,x,y=map(int,input().split())

def check(idx):
    appear=[-1]*(2*n)
    for i in range(idx):
        if appear[arr[i]]==-1:
            appear[arr[i]]=i
        else:
            if i-appear[arr[i]]!=arr[i]+1:
                return False
    if arr[x-1]!=0 and arr[y-1]!=0:
        if arr[x-1]!=arr[y-1]: return False
    return True

def bt(idx):
    if idx==2*n:
        if arr[x-1]==arr[y-1]:
            return 1
        else:
            return 0
    res=0
    if arr[idx]!=0:
        res+=bt(idx+1)
    else:
        for i in range(1,n+1):
            if use[i]==0:
                if idx+i+1<2*n and arr[idx+i+1]==0:
                    use[i]=1
                    arr[idx]=i
                    arr[idx+i+1]=i
                    res+=bt(idx+1)
                    arr[idx]=0
                    arr[idx+i+1]=0
                    use[i]=0
    return res
        

use=[0]*(n+1)
arr=[0]*(2*n)
fix=y-x-1
use[fix]+=1
arr[y-1]=arr[x-1]=fix
print(bt(0))


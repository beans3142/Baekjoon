from time import *
from sys import *
setrecursionlimit(100000)
input=stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
now=time()
rdiag={}
for i in range(-n,n):
    rdiag[i]=0
ans=0
able=2*n-1
mxlen=2*n-1

def bt(idx,cnt):
    global ans
    left=0
    if idx==mxlen:
        ans=max(ans,cnt)
        return

    for i in range(idx,mxlen):
        for j in range(i+1):
            k=i-j
            if -1<j<n and -1<k<n and rdiag[k-j]==0:
                left+=1
                break
                
    if left+cnt<=ans:
        return
    
    for i in range(idx+1):
        j=idx-i
        if -1<i<n and -1<j<n and arr[i][j]==1 and rdiag[j-i]==0:
            rdiag[j-i]=1
            bt(idx+1,cnt+1)
            rdiag[j-i]=0
    bt(idx+1,cnt)

bt(0,0)

print(ans)
print(time()-now)

'''
7
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
8
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
'''

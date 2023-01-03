def bt(idx,cnt=0):
    if cnt==m:
        print(*ans)
        return
    for i in range(n):
        ans[cnt]=arr[i]
        bt(i,cnt+1)
        ans[cnt]=0
        
n,m=map(int,input().split())
arr=sorted(map(int,input().split()))
ans=[0]*m
bt(0,0)

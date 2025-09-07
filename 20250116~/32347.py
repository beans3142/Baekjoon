N,K=map(int,input().split())
arr=[1]+list(map(int,input().split()))+[1]

bef=0
res=1
for i in range(1,N+2):
    if arr[i]==1:
        res=max(res,i-bef-1)
        bef=i

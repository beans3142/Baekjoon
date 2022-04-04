from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
arr=[1 for i in range(n+1)]
cnt=0
for i in range(2,n+1):
    if arr[i]==0:
        continue
    for j in range(i,n+1,i):
        if arr[j]==1:
            cnt+=1
        arr[j]=0
        if cnt==k:
            print(j)
            exit()
    

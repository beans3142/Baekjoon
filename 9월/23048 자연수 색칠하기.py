from sys import stdin
input=stdin.readline
n=int(input())
inf=10**10
arr=[inf]*(n+1)
arr[0]=arr[1]=1
k=1
for i in range(2,n+1):
    if arr[i]!=inf:
        continue
    k+=1
    arr[i]=k
    for j in range(i*2,n+1,i):
        arr[j]=k
        
print(len(set(arr)))
for i in range(1,n+1):
    print(arr[i],end=' ')

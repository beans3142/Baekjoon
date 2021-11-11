n=int(input())
arr=list(map(int,input().split()))
s=[arr[0]]
print(s[0],end=' ')
for i in range(1,n):
    print(arr[i]*(i+1)-arr[i-1]*i,end=' ')

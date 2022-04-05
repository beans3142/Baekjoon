n=int(input())
b=list(map(int,input().split()))
a=[0]*n
a[0]=b[0]
for i in range(1,n):
    a[i]=b[i]*(i+1)-sum(a[:i])

print(*a)

from sys import stdin
input=stdin.readline

k=int(input())
mob=[0]*(1000001)

def mobius():
    mob[1]=1
    for i in range(1,1000001):
        if mob[i]!=0:
            for j in range(i*2,1000001,i):
                mob[j]-=mob[i]

def sf(n):
    k=0
    for i in range(1,n+1):
        if i**2>n:
            break
        k+=mob[i]*(n//(i**2))
    return k

l=0
r=20000000000
mobius()
while l+1<r:
    mid=(l+r)//2
    p=sf(mid)
    if sf(mid)<k:
        l=mid
    else:
        r=mid

print(r)

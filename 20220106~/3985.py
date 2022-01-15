from sys import stdin
input=stdin.readline

l=int(input())
n=int(input())

mx=0
mx_idx=0
mx_ideal=0
mx_ideal_idx=0

cake=[1]*(l+1)
for _ in range(n):
    p,k=map(int,input().split())
    if k-p>mx_ideal:
        mx_ideal=k-p
        mx_ideal_idx=_+1
    get=0
    for i in range(p,k+1):
        if cake[i]==1:
            get+=1
            cake[i]=0
    if get>mx:
        mx_idx=_+1
        mx=get

print(mx_idx)
print(mx_ideal_idx)

from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
arr=list(map(int,input().split()))
loc=[]
for i in range(n):
    if arr[i]==1:
        loc.append(i)

mnsize=10**9
s=0
e=k-1

while e<len(loc):
    size=loc[e]-loc[s]
    mnsize=min(size,mnsize)
    s+=1
    e+=1

print(mnsize+1 if mnsize != 10**9 else -1)

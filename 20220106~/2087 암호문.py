from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
hf=defaultdict(int)

arr=[int(input()) for i in range(n)]
target=int(input())

def fs(x,idx,bit):
    for i in range(idx,n//2):
        nbit=1<<i
        hf[x+arr[i]]=bit+nbit
        fs(x+arr[i],i+1,bit+nbit)

fs(0,0,0)

def bs(x,idx,bit):
    for i in range(idx,n):
        nbit=1<<i
        key=target-x-arr[i]
        if hf[key]:
            hf[target]=bit+nbit+hf[key]
        bs(x+arr[i],i+1,bit+nbit)

bs(0,n//2,0)
ans=bin(hf[target])[::-1][:-2]
ans=ans+(n-len(ans))*'0'
print(ans)

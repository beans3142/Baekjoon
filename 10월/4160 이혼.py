from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
hf=defaultdict(list)

arr=sorted([int(input()) for i in range(n)])
s=sum(arr)//2

def fs(x,idx,bit):
    for i in range(idx,n//2):
        nbit=1<<i
        hf[x+arr[i]].append(bit+nbit)
        fs(x+arr[i],i+1,bit+nbit)

fs(0,0,0)

def bs(x,idx,bit):
    for i in range(idx,n):
        nbit=1<<i
        key=x+arr[i]
        if key<s:
            for v in hf[key]:
                if nbit & v==0:
                    ans=max(ans,nbit)
        bs(x+arr[i],i+1,bit+nbit)

bs(0,n//2,0)
ans=ans+(n-len(ans))*'0'
print(ans)

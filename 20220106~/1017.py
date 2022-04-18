from sys import stdin
from collections import *
input=stdin.readline

prime=[1]*(2001)
for i in range(2,2001):
    if prime[i]==0:
        continue
    for j in range(i+i,2001,i):
        prime[j]=0

def dfs(x):
    if vi[x] or x==start:
        return False
    vi[x]=True
    for i in oe[x]:
        if(match[i]==0 or dfs(match[i])):
            match[i]=x
            match[x]=i
            return True
    return False

n=int(input())
arr=list(map(int,input().split()))
vi=[False]*2001
odd=[]
even=[]
start=arr[0]
for a in arr:
    c=a+start+1
    if c%2:
        odd.append(a)
    else:
        even.append(a)

oe={i:[] for i in odd}

for i in odd:
    for j in even:
        if prime[i+j]:
            oe[i].append(j)

ans=[]

cnt=0
for _ in oe[start]:
    cnt=1
    match=[0]*2001
    match[start]=_
    match[_]=start
    for i in range(1,len(odd)):
        i=odd[i]
        for j in range(2001):
            vi[j]=False
        if dfs(i):
            cnt+=1
    if cnt==len(odd):
        ans.append(match[start])
        
if ans and len(odd)==len(even):
    for i in sorted(set(ans)):
        print(i,end=' ')
else:
    print(-1)

from sys import stdin
from math import *
input=stdin.readline

n,k=map(int,input().split())
card=list(map(int,input().split()))
vi=[0]*20
able=[]
ans=0

for i in range(k):
    cnt=0
    for j in range(k):
        if card[i]%card[j]==0:
            cnt+=1
            if cnt>1:
                break
    if cnt==1:
        able.append(card[i])
        

def bt(idx,nums,depth):
    global ans
    for i in range(idx,len(able)):
        if vi[i]==0:
            vi[i]=1
            lc=lcm(nums,able[i])
            bt(i,lc,depth+1)
            val=n//(lc)
            if depth%2==0:
                val=-val
            ans+=val
            vi[i]=0

bt(0,1,1)
print(ans)

from sys import stdin
from math import lcm
input=stdin.readline

k,l,r=map(int,input().split())
card=list(set(map(int,input().split())))
vi=[0]*20
able=[]
ans=[0,0]

for i in range(len(card)):
    cnt=0
    for j in range(len(card)):
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
            val_l=(l-1)//(lc)
            val_r=r//(lc)
            if depth%2==0:
                val_l=-val_l
                val_r=-val_r
            ans[0]+=val_l
            ans[1]+=val_r
            vi[i]=0

bt(0,1,1)

print(ans[1]-ans[0])

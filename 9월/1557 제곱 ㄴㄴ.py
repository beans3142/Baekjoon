from sys import stdin,setrecursionlimit
from math import *
setrecursionlimit(5000)
input=stdin.readline

k=int(input())
vi=[0]*31701
ans=0
numlist=[i for i in range(2,31700)]
able=[]
for i in range(2,31700):
    ab=True
    for j in range(2,i):
        if i%j==0:
            ab=False
            break
    if ab:
        able.append(i)


def bt(idx,nums,depth):
    global ans
    for i in range(idx,len(able)):
        if vi[i]==0:
            vi[i]=1
            lc=lcm(nums,able[i])
            bt(i,lc,depth+1)
            val=m//(lc)
            if depth%2==0:
                val=-val
            ans+=val
            vi[i]=0


bt_result=[]

for i in range(
bt(0,1,1)
print(ans)

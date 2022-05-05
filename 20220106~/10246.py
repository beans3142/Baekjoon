from sys import stdin
from bisect import *
input=stdin.readline

presum=[0,2]
cnt=[1]*1000001

for i in range(2,1000000):
    presum.append(i+1+presum[-1])

for i in range(1,500001):
    for j in range(i-1,0,-1):
        now=presum[i]-presum[j]+j+1
        if now>1000000:
            break
        cnt[now]+=1

cnt[1]=0
    
while True:
    n=int(input())
    if n==0:
        break
    print(cnt[n])
    


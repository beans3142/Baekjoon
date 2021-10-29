from sys import stdin
from math import sqrt
from collections import defaultdict
input=stdin.readline

n=int(input())
prime=[]


for i in range(2,int(sqrt(n))+1):
    if n%i==0:
        prime.append(i)

# 포함배재 쓰려는데 어떻게 썼더라?
# 무지성 dfs
ans=n-1

def inc_exc(num,idx,dep):
    global ans
    for i in range(idx,len(prime)):
        nnum=num+prime[i]
        if dep%2==1:
            ans-=n//nnum
        else:
            ans+=n//nnum
        inc_exc(nnum,i+1,dep+1)
        
inc_exc(0,0,1)
print(ans)

# 이렇게 못푼다. 포함배재로는 안될듯...

from sys import stdin
from math import gcd
input=stdin.readline

prime=[1]*31624
pl=[]

for i in range(2,31624):
    if prime[i]==0:
        continue
    pl.append(i)
    for j in range(i+i,31624,i):
        prime[j]=0


while True:
    n,k=map(int,input().split())
    ans=0
    

# 아 모르겠다 시험공부나 해야지

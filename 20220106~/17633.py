from sys import stdin,setrecursionlimit
from random import randrange
from math import gcd
input=stdin.readline
setrecursionlimit(10000)
base={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,61,67,71,73}


def pow(x,n,d):
    v=1
    while n>0:
        if n%2==1:
            v=v*x%d
        x=x*x%d
        n//=2
    return v
        

def mrt(n,b,s,t):
    x=pow(b,t,n)
    if x==1 or x==n-1:
        return 1
    else:
        for i in range(s):
            if x==n-1:
                return 1
            x=pow(x,2,n)
        return 0

def isp(n):
    if n in base:
        return True
    if n<2 or n%2==0:
        return False
    s=0
    t=n-1
    while t%2==0:
        s+=1
        t//=2
    for i in base:
        if not mrt(n,i,s,t):
            return False
    return True

def pollard_rho(x):
    if x==1:
        return 1
    
    if x%2==0:
        pollard_rho(x//2)
        return 2
    
    if isp(x):
        return x
    n1=n2=randrange(2,x)
    c=randrange(1,x)
    r=1
    while r==1:
        n1=((n1**2)%x+c)%x
        n2=((n2**2%x)+c)%x
        n2=((n2**2%x)+c)%x
        r=gcd(abs(n1-n2),x)
        if r==x:
            n1=n2=randrange(2,x)
            c=randrange(1,x)
            r=1
    if isp(r):
        return r
    return pollard_rho(r)

def factorization(n):
    while n>1:
        factor=pollard_rho(n)
        ans.append(factor)
        n//=factor
        

def bit1(x):
    cnt=0
    while x:
        cnt+=x%2
        x//=2
    return cnt

def iae(size):
    cnt=0
    for i in range(1,1<<size):
        tmp=1
        for j in range(size):
            if i&(1<<j):
                tmp*=ans[j]
        if bit1(i)%2:
            cnt+=n//tmp
        else:
            cnt-=n//tmp
    return cnt



ans=[]
n=int(input())
while n%4==0:
    n//=4
if n%8==7: #라그랑주 4 제곱
    print(4)
    exit()

factorization(n)

s=set()
for i in ans:
    if i in s:
        s.remove(i)
    else:
        s.add(i)

for i in s:
    if i%4==3:
        print(3)
        exit()

if int(n**0.5)*int(n**0.5)==n:
    print(1)
    exit()
else:
    print(2)

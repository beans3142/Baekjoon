from sys import stdin,setrecursionlimit
from random import randint
from collections import defaultdict
from math import gcd,factorial
input=stdin.readline
setrecursionlimit(100000)


base={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,61,67}

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
    global cnt
    if x==1:
        return
    if x%2==0:
        ans.append(2)
        pollard_rho(x//2)
        return
    
    if isp(x):
        ans.append(x)
        return

    while True:
        c=randint(1,x-1)
        t=1
        r=1
        g=1
        able=True
        while g==1:
            t=(t**2+c)%x
            r=((r**4)+(2*c*(r**2)+(c**2)+c))%x
            g=gcd(abs(t-r),x)
            if g==x:
                able=False
                break
        if able:
            pollard_rho(g)
            pollard_rho(x//g)
            return
        
ans=[]
pollard_rho(int(input()))
print(*ans,sep='\n')

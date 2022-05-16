from sys import stdin,setrecursionlimit
from collections import defaultdict
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
        ans[factor]+=1
        n//=factor

def bt(n,idx):
    able=True
    for i in range(len(arr)):
        if arr[i]%n!=0 and n%arr[i]!=0:
            able=False
            break
    if able and l<=n<=h:
        cc.append(n)
        return
    if idx<len(li):
        bt(n*li[idx],idx+1)
        bt(n,idx+1)
    
            
    
        
for _ in range(int(input())):
    n,l,h=map(int,input().split())
    case=defaultdict(list)
    arr=list(map(int,input().split()))
    for i in arr:
        if i==1:
            n-=1
            continue
        ans=defaultdict(int)
        factorization(i)
        for j in ans:
            case[j].append(ans[j])
    
    gcd=1
    lcd=1
    mn=1
    li=list(case)
    cc=[]
    bt(1,0)
    if cc:
        print(f'Case #{_+1}: {min(cc)}')
        continue
    
    for i in case:
        lcd*=i**(max(case[i]))

    val=l//lcd*lcd
    if l%lcd:
        val+=lcd
    if l<=val<=h:
        print(f'Case #{_+1}: {val}')
    else:
        print(f'Case #{_+1}: NO')


from sys import stdin
from math import gcd
input=stdin.readline

def getpi(s):
    j=0
    m=len(s)
    pi=[0]*m
    for i in range(1,m):
        while j>0 and s[i]!=s[j]:
            j=pi[j-1]
        if s[i]==s[j]:
            pi[i]=j+1
            j+=1
    return pi

def kmp(s,p):
    ans=[]
    pi=getpi(p)
    n=len(s)
    m=len(p)
    j=0
    for i in range(n):
        while j>0 and s[i]!=p[j]:
            j=pi[j-1]
        if s[i]==p[j]:
            if j==m-1:
                ans.append(i-m+1)
                j=pi[j]
            else:
                j+=1
    return ans

n=int(input())
s=''.join(input().rstrip().split())
m=''.join(input().rstrip().split())
pi=getpi(s*2)
ans=kmp((s*2)[:-1],m)

print(len(ans)//gcd(len(ans),n),'/',n//gcd(len(ans),n),sep='')


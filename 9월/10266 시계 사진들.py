from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
s=list(map(int,input().split()))
p=list(map(int,input().split()))

def getpi(p):
    v=[0]*len(p)
    j=0
    for i in range(1,len(p)):
        while j>0 and p[i]!=p[j]:
            j=p[j-1]
        if p[i]==p[j]:
            j+=1
            v[i]=j
    return v

def kmp(s,p):
    pi=getpi(p)
    j=0
    for i in range(len(s)):
        while j>0 and s[i]!=p[j]:
            j=pi[j-1]
        if s[i]==p[j]:
            if j==len(p)-1:
                return True:
            else:
                j+=1
    return False:

c1=[0]*360000
c2=[0]*360000

for i in s:
    c1[i]=1
for i in p:
    c2[i]=1

c1+=c1

if kmp(c1,c2):
    print("possible")
else:
    print("impossible")

from sys import stdin
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
                return 1
            else:
                j+=1
    return 0


S=input().rstrip()
P=input().rstrip()

print(kmp(S,P))

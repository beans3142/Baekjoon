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

n=int(input())
S=input().rstrip()

ans=getpi(S)
print(n-ans[n-1])

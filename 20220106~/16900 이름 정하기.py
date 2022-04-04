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

s,n=input().rstrip().split()
ans=getpi(s)
print(len(s)*int(n)-ans[-1]*(int(n)-1))

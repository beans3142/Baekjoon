from sys import stdin
from collections import deque
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

def kmp(s_arr):
    cmp=deque([])
    for i in range(M):
        cmp.append(mncode[i])
    idx=M
    while True:
        pi=getpi(cmp)
        cmp2=[0]*M
        pi2=[0]*M
        for i in range(M):
            cmp2[~i]=cmp[i]
            pi2[~i]=pi[i]
        for s in s_arr:
            ans=[]
            ans2=[]
            n=len(s)
            p=cmp
            p2=cmp2
            j=0
            j2=0
            for i in range(n):
                while j>0 and s[i]!=p[j]:
                    j2=pi[j-1]
                while j2>0 and s[i]!=p2[j]:
                    j2=pi2[j-1]
                if s[i]==p2[j]:
                    if j2==M-1:
                        ans2.append(i-M+1)
                        j2=pi2[j2]
                    else:
                        j2+=1
            print(ans)
            print(ans2)
        cmp.popleft()
        cmp.append(mncode[idx])
        idx+=1
        if idx==mncase:
            break

N,M=map(int,input().split())
mncase=1000000000000000
arr=[]
for i in range(N):
    now_len=int(input())
    now_code=input().rstrip().split()
    if now_len<mncase:
        try:
            arr.append(mncode)
        except:
            pass
        mncase=now_len
        mncode=now_code
    else:
        arr.append(now_code)
kmp(arr)

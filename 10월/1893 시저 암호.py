from sys import stdin
input=stdin.readline
'''
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
'''
def getpi():
    # 원문 pi
    pref = 0
    pi = [0] * (len(origin) + 1)
    for suff in range(1, len(origin)):
        while pref > 0 and origin[pref] != origin[suff]:
            pref = pi[pref - 1]

        if origin[pref] == origin[suff]:
            pref += 1
            pi[suff] = pref

            if pref == len(origin):
                break
    return pi
def kmp(s,p):
    ans=[]
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
for _ in range(n):
    order=input().rstrip()
    ch={}
    l=len(order)
    ans=[]
    for i in range(l):
        ch[order[i]]=order[(i+1)%l]
    w=list(input().rstrip())
    pi=getpi(w)
    s=input().rstrip()
    for i in range(l):
        cnt=kmp(w,s)
        if len(cnt)==1:
            ans.append(i)

        print(w)
        for j in range(len(w)):
            w[j]=ch[w[j]]
        print(w)
    if not ans:
        print('no solution')
    elif len(ans)==1:
        print(f'unique: {ans[0]}')
    else:
        print(f'ambiguous: ',end='')
        print(*ans)

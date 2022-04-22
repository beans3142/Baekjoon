from sys import stdin
input=stdin.readline

n=int(input())

def power(a, n):
    if n == 0:
        return 1
    
    x = power(a, n//2)

    if n % 2 == 0:
        return (x * x)%(10**9+7)
    
    else:
        return (x * x * a)%(10**9+7)
wc=[0]*n
ec=[0]*n
ecnt=0
wcnt=0

fac=[0,0]+[(power(2,i)-i-1)%(10**9+7) for i in range(2,n+1)]

s=input().rstrip()

for i in range(n):
    if s[~i]=='W':
        wcnt+=1
    if s[i]=='E':
        ecnt+=1
    ec[i]=ecnt
    wc[~i]=wcnt

ans=0
for i in range(n):
    if s[i]=='H':
        ans+=fac[ec[-1]-ec[i]]*(wc[0]-wc[i])

print(ans%(10**9+7))

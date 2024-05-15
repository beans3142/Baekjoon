n=int(input())
a=list(map(int,input().split()))
r=[-1]*n
s=[]
for i in range(n):
    N=a.pop()
    while s and s[-1]<=N:
        s.pop()
    if s:
        r[~i]=s[-1]
    s.append(N)
print(*r)

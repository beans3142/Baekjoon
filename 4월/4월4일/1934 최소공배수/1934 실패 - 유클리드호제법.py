t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    n,m=max(a,b),min(a,b)
    r=n%m
    if r ==0:
        print(n)
        continue
    while r!=0:
        r=n%m
        n=m
        m=r
    print(a*b//n)

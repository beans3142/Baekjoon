a,b=map(int,input().split())
n=max(a,b)
m=min(a,b)
r=n%m
while r!=0:
    n=m
    m=r
    r=n%m

print(m)
print(a*b//m)

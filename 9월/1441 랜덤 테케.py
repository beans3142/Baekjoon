from random import *
n=randint(1,18)
a=randint(1,10**2)
b=randint(1,10**2)
l=min(a,b)
r=max(a,b)
print(n,l,r)
for i in range(n):
    print(randint(1,10**2),end=' ')

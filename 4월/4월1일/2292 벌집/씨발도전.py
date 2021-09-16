from math import *
N=int(input())
x=0
if N==1:
    x=1
elif N>1:
    N-=1
    while N>0:
        N-=6*x
        x+=1
print(x)

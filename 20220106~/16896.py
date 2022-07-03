from sys import stdin
from math import log2,floor
input=stdin.readline

for i in range(int(input())):
    n=int(input())
    if n%2:
        n=2*n-2
        able=False
        while 0<n:
            N=int(log2(n))
            if N%2:
                able=True
                break
            n-=2**N
        if able:
            print('cubelover')
        else:
            print('koosaga')
    else:
        print('cubelover')
        


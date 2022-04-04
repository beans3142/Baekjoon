import math as m

A,B,C=map(int,input().split())

if C<=B:
    print(-1)
elif (A/(C-B))%1==0:
    print(int(A/(C-B)+1))   
else:
    print(m.ceil(A/(C-B)))


#A + Bx < Cx => A < (C-B)x => A/(C-B) < X

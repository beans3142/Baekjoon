import math as m

A,B,V=map(int,input().split())

print(m.ceil((V-B)/(A-B)))

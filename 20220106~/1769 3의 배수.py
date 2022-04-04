from sys import stdin
from math import log
input=stdin.readline

x=int(input())
tmpt=0

while len(x)>1:
    x=list(sum(list(x)))
    tmpt+=1

print(tmpt)
print('YES' if x[0]%3==0 else 'NO')

from sys import stdin
from math import ceil
input=stdin.readline
aa,ab=map(int,input().split())
ba,bb=map(int,input().split())
while ab>0 and bb>0:
    ab-=ba
    bb-=aa

if ab<=0 and bb<=0:
    print("DRAW")
elif ab>0:
    print("PLAYER A")
else:
    print("PLAYER B")

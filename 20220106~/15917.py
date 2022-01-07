from sys import stdin
from collections import defaultdict
input=stdin.readline
two=defaultdict(int)
one=1
for i in range(32):
    two[one]=1
    one*=2
Q=int(input())
for i in range(Q):
    print(two[int(input())])
    

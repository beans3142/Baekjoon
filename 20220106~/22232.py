from sys import stdin
from collections import defaultdict
input=stdin.readline

def div(filename):
    name,exten=filename.split('.')
    return name,insik[exten],exten
    

n,m=map(int,input().split())
arr=[input().rstrip() for i in range(n)]
insik=defaultdict(int)
for i in range(m):
    insik[input().rstrip()]=-1
arr.sort(key=div)
for i in arr:
    print(i)

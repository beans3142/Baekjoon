from sys import stdin
from collections import defaultdict
from math import gcd
input=stdin.readline

def gettilt(x,y):
    
    if x==0:
        if y>0:
            return '위'
        return '아래'
    
    if y==0:
        if x>0:
            return '오른쪽'
        return '왼쪽'
    div=gcd(x,y)
    return (x//div,y//div)
        

n=int(input())
arr=[map(int,input().split()) for i in range(n)]
dd=defaultdict(int)
for i in arr:
    dd[gettilt(next(i),next(i))]+=1

mx=0
for i in dd:
    mx=max(dd[i],mx)

print(mx)

import math
from sys import stdin
input=stdin.readline
inf=float('inf')

pi = 3.14159265358979323846

def dist(x, y):
    return x ** 2 + y ** 2

def angle(x, y):
    t = math.atan2(y, x)
    return t + 2 * pi if t < 0 else t

def getangle(d1,d2):
    da=angle(*d1)
    db=angle(*d2)
    return (da-db)*180/pi

n=int(input())
mx=0
for i in range(n):
    x,y=map(int,input().split())
    dis=dist(x,y)
    if mx<dis:
        mx=dis
        arr=[(x,y)]
    elif mx==dis:
        arr.append((x,y))

if len(arr):
    print("360.0000000")
    exit()

ans=0.0
for i in range(len(arr)):
    ans=max(ans,getangle(arr[i],arr[i-1]))

print(f"{ans:.8f}")

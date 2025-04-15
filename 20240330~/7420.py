from sys import stdin
from math import pi
input=stdin.readline
inf=float('inf')

def sim_arctan(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if dy!=0: tilt=-dx/dy if dx!=0 else 0
    else: tilt=-inf
    return tilt

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def getdist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def conv_hull(arr):
    arr = sorted(arr, key=lambda x: (x[1], x[0]))
    le = len(arr)
    if le < 3:
        return len(arr)
    st = arr[0]
    arr.pop(0)
    arr = [st]+sorted(arr, key=lambda x: sim_arctan(st[0],st[1],x[0],x[1]))
    
    stack=[st,arr[1]]
    for i in range(2,le):
        nxt=arr[i]
        while len(stack)>=2 and ccw(*stack[-2],*stack[-1],*nxt)<=0:
            stack.pop()
        stack.append(arr[i])

    return stack

def getAns():
    st=conv_hull(arr)
    dist=0
    for i in range(len(st)):
        dist+=getdist(*st[i],*st[i-1])
    return round(dist+2*pi*L)
        

n,L=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
st=conv_hull(arr)
print(getAns())

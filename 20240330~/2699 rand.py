from sys import stdin
from random import *
input=stdin.readline
inf=1e10

def sim_arctan(x2,y2,x1,y1):
    dx=x2-x1
    dy=y2-y1
    if dy!=0: tilt=-dx/dy if dx!=0 else 0
    else: tilt=inf
    return -tilt

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def conv_hull(arr):
    arr = sorted(arr, key=lambda x: (-x[1], x[0]))
    le = len(arr)
    if le < 3:
        return arr
    st = arr[0]
    arr.pop(0)
    arr = [st]+sorted(arr, key=lambda x: sim_arctan(st[0],st[1],x[0],x[1]))
    
    stack=[st,arr[1]]
    for i in range(2,le):
        nxt=arr[i]
        while len(stack)>=2 and ccw(*stack[-2],*stack[-1],*nxt)>=0:
            stack.pop()
        stack.append(arr[i])

    return stack

for _ in range(int(input())):
    n=randint(3,100)
    arr=[]
    for i in range(round(n/5)):
        ls=[randint(-20,20) for i in range(10)]
        for j in range(0,len(ls),2):
            arr.append([ls[j],ls[j+1]])
    ans=conv_hull(arr)
    print(len(ans))
    for x,y in ans:
        print(x,y)

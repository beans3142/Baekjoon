from sys import stdin
input=stdin.readline
inf=float('inf')

def sim_arctan(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if dy!=0: tilt=dy/dx if dx!=0 else inf
    elif dy==dx==0: return -inf
    else: tilt=0
    return tilt

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def conv_hull(arr):
    arr = sorted(arr, key=lambda x: (x[1], x[0]))
    arr.sort()
    le = len(arr)
    if le < 3:
        return arr
    st = arr[0]
    arr.pop(0)
    arr = [st]+sorted(arr, key=lambda x: (sim_arctan(st[0],st[1],x[0],x[1])))
    ans=[]
    stack=[st,arr[1]]
    for i in range(2,le):
        nxt=arr[i]
        while len(stack)>=2 and ccw(*stack[-2],*stack[-1],*nxt)<=0:
            stack.pop()
        stack.append(arr[i])

    return stack

n=int(input())
arr=[input().rstrip().split() for i in range(n)]
narr=[]
for i in arr:
    if i[-1]=='Y':
        narr.append((int(i[0]),int(i[1])))

for i in conv_hull(narr):
    print(*i)

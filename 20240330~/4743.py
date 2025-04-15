import sys
input = sys.stdin.readline
inf=float('inf')

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def sim_arctan(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if dy!=0: tilt=-dx/dy if dx!=0 else 0
    else: tilt=-inf
    return tilt

def conv_hull(arr):
    arr = sorted(arr, key=lambda x: (x[1], x[0]))
    le = len(arr)
    if le < 3:
        return arr
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

def inter(x1, y1, x2, y2, x3, y3, x4, y4):
    a1 = ccw(x1, y1, x2, y2, x3, y3)
    a2 = ccw(x1, y1, x2, y2, x4, y4)
    a3 = ccw(x3, y3, x4, y4, x1, y1)
    a4 = ccw(x3, y3, x4, y4, x2, y2)
    if a1 * a2 < 0 and a3 * a4 < 0:
        d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if d == 0: return None
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d
        return px, py
    return None

def inside(p, poly):
    cnt = 0
    x, y = p
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if ccw(x1, y1, x2, y2, x, y) == 0 and min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
            return True
        if y1 <= y < y2 or y2 <= y < y1:
            intersect_x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < intersect_x:
                cnt += 1
    return cnt % 2 == 1


def area(pts):
    hull = conv_hull(pts)
    n = len(hull)
    ans = 0
    for i in range(n):
        x1, y1 = hull[i]
        x2, y2 = hull[(i + 1) % n]
        ans += x1 * y2 - x2 * y1
    return abs(ans) / 2


def triangle_area(pts):
    hull = conv_hull(pts)
    n = len(hull)
    ans = 0
    for i in range(1, n - 1):
        x1, y1 = hull[0]
        x2, y2 = hull[i]
        x3, y3 = hull[i + 1]
        ans += abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    return ans

idx=1
while True:
    n, m = map(int, input().split())
    if n==m==0:
        break
    arr1=[]
    for i in range(n):
        a,b,c,d=map(int,input().split())
        arr1+=[(a,b),(c,b),(c,d),(a,d)]
    arr2=[]
    for i in range(m):
        a,b,c,d=map(int,input().split())
        arr2+=[(a,b),(c,b),(c,d),(a,d)]
    poly1 = conv_hull(arr1)
    poly2 = conv_hull(arr2)

    res = []
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            p1, p2 = poly1[i], poly1[(i + 1) % len(poly1)]
            p3, p4 = poly2[j], poly2[(j + 1) % len(poly2)]
            p = inter(*p1, *p2, *p3, *p4)
            if p: res.append(p)

    for p in poly1:
        if inside(p, poly2): res.append(p)
    for p in poly2:
        if inside(p, poly1): res.append(p)

    if res:
        print(f"Case {idx}: It is not possible to separate the two groups of vendors.\n")
    else:
        print(f"Case {idx}: It is possible to separate the two groups of vendors.\n")
    idx+=1

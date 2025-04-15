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
    x, y = p
    n = len(poly)
    if n == 0:
        return False
    if n == 1:
        return p == poly[0]
    if n == 2:
        return ccw(*poly[0], *poly[1], x, y) == 0 and min(poly[0][0], poly[1][0]) <= x <= max(poly[0][0], poly[1][0]) and min(poly[0][1], poly[1][1]) <= y <= max(poly[0][1], poly[1][1])
    
    def orientation(a, b, c):
        val = ccw(*a, *b, *c)
        if val > 0:
            return 1
        elif val < 0:
            return -1
        else:
            return 0

    if orientation(poly[0], poly[1], p) < 0 or orientation(poly[0], poly[-1], p) > 0:
        return False

    left = 1
    right = n - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if orientation(poly[0], poly[mid], p) >= 0:
            left = mid
        else:
            right = mid
    
    o = orientation(poly[left], poly[left + 1], p)
    return o >= 0


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

n=int(input())
points1=[tuple(map(int,input().split())) for i in range(n)]
points2=[tuple(map(int,input().split())) for i in range(n)]
poly1=conv_hull(points1)
poly2=conv_hull(points2)
cnt1=0
cnt2=0
for p in points2:
    if inside(p,poly1):
        cnt1+=1
for p in points1:
    if inside(p,poly2):
        cnt2+=1
print(cnt1,cnt2)

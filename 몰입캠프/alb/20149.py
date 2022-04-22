from sys import stdin
input = stdin.readline
points = []
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

points.append([x1, y1])
points.append([x2, y2])
points.append([x3, y3])
points.append([x4, y4])

def intersection(a, b, c, d):
    if ccw(*a, *b, *c) * ccw(*a, *b, *d) == 0:
        if ccw(*c, *d, *a) * ccw(*c, *d, *b) == 0:
            if a > b:
                a, b = b, a
            if c > d:
                c, d = d, c
            if b >= c and a <= d:
                return True
            return False
    if ccw(*a, *b, *c) * ccw(*a, *b, *d) <= 0:
        if ccw(*c, *d, *a) * ccw(*c, *d, *b) <= 0:
            return True
    return False

def ccw(x1,y1,x2,y2,x3,y3):
    return (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)

if intersection(*points):
    print(1)
    try:
        x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        print(x, y)
    except:
        if points[0] > points[1]:
            points[0], points[1] = points[1], points[0]
        if points[2] > points[3]:
            points[2], points[3] = points[3], points[2]
        if points[1] == points[2]:
            print(points[1][0], points[1][1])
        elif points[0] == points[3]:
            print(points[0][0], points[0][1])
else:
    print(0)

from sys import stdin
import math

input = stdin.readline

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def convex_hull(points):
    points = sorted(points)
    hull = []
    
    for p in points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    
    lower = len(hull)
    for p in reversed(points):
        while len(hull) > lower and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    
    return hull[:-1]  # 마지막 점은 중복되므로 제외

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def calculate_perimeter(hull, trees):
    perimeter = 0
    for i in range(len(hull)):
        perimeter += dist(hull[i], hull[(i + 1) % len(hull)])
    
    for x, y, r in trees:
        inside = False
        for h in hull:
            if dist(h, (x, y)) < r:  # 원의 중심이 헐 내부에 있는지 체크
                inside = True
                break
            
        if inside:
            perimeter += 2 * math.pi * r  # 원의 전체 둘레 추가
        else:
            # 원과 헐의 접점 계산
            for i in range(len(hull)):
                a, b = hull[i], hull[(i + 1) % len(hull)]
                d = dist(a, b)
                h = abs((b[0] - a[0]) * (a[1] - y) - (b[1] - a[1]) * (a[0] - x)) / d  # 점과 선분의 거리
                if h < r:  # 접하는 경우
                    perimeter += 2 * math.sqrt(r**2 - h**2)  # 접선 길이 추가

    return perimeter

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    trees = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        trees.append((x, y, r))
    
    points = [(x, y) for x, y, r in trees]
    hull = convex_hull(points)
    total_perimeter = calculate_perimeter(hull, trees)
    
    results.append(f"{total_perimeter:.5f}")

print("\n".join(results))

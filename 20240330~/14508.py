import math

def cross_product(v1, v2):
    return (v1[1] * v2[2] - v1[2] * v2[1], 
            v1[2] * v2[0] - v1[0] * v2[2], 
            v1[0] * v2[1] - v1[1] * v2[0])

def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def vector_subtract(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])

def vector_length(v):
    return math.sqrt(dot_product(v, v))

def distance_point_to_line(point, line_point1, line_point2):
    line_vec = vector_subtract(line_point2, line_point1)
    point_vec = vector_subtract(point, line_point1)
    cross_prod = cross_product(line_vec, point_vec)
    return vector_length(cross_prod) / vector_length(line_vec)

def convex_hull(points):
    # Using Gift wrapping algorithm to find the convex hull
    hull = []
    start = min(points)
    point_on_hull = start
    while True:
        hull.append(point_on_hull)
        endpoint = points[0]
        for j in range(1, len(points)):
            if endpoint == point_on_hull or not is_left_turn(point_on_hull, endpoint, points[j]):
                endpoint = points[j]
        point_on_hull = endpoint
        if endpoint == start:
            break
    return hull

def is_left_turn(p1, p2, p3):
    return cross_product(vector_subtract(p2, p1), vector_subtract(p3, p1)) > (0, 0, 0)

def find_minimum_cylinder(points):
    hull_points = convex_hull(points)
    
    min_volume = float('inf')
    
    for i in range(len(hull_points)):
        for j in range(i + 1, len(hull_points)):
            p1 = hull_points[i]
            p2 = hull_points[j]
            height = vector_length(vector_subtract(p1, p2))
            
            max_radius = 0
            for point in points:
                if point != p1 and point != p2:
                    radius = distance_point_to_line(point, p1, p2)
                    max_radius = max(max_radius, radius)
                    
            volume = math.pi * max_radius**2 * height
            if volume < min_volume:
                min_volume = volume
    
    return min_volume

# Read input
n = int(input())
points = []
for _ in range(n):
    x, y, z = map(int, input().split())
    points.append((x, y, z))

result = find_minimum_cylinder(points)
print(f"{result:.6f}")

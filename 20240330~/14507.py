import math
import numpy as np

# Cross product of two vectors a and b
def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]

# Dot product of two vectors a and b
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

# Subtract vector b from vector a
def subtract(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

# Norm of vector a
def norm(a):
    return math.sqrt(dot(a, a))

# Project point p onto direction dir
def project(p, dir):
    scalar = dot(p, dir) / dot(dir, dir)
    return [scalar * d for d in dir]

# Function to compute the minimum enclosing cylinder volume
def smallest_enclosing_cylinder(points):
    n = len(points)
    min_volume = float('inf')

    for i in range(n):
        for j in range(i + 1, n):
            # Direction vector between points[i] and points[j]
            direction = subtract(points[j], points[i])
            direction_norm = norm(direction)
            if direction_norm == 0:
                continue
            direction = [d / direction_norm for d in direction]

            # Project all points onto the plane orthogonal to the direction vector
            projections = [subtract(p, project(p, direction)) for p in points]
            projection_norms = [norm(proj) for proj in projections]

            # Find the maximum projection norm (radius of the cylinder)
            radius = max(projection_norms)

            # Find the height of the cylinder along the direction vector
            heights = [dot(p, direction) for p in points]
            height = max(heights) - min(heights)

            # Calculate the volume of the cylinder
            volume = math.pi * radius**2 * height
            min_volume = min(min_volume, volume)

    return min_volume

# Example usage:
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
min_volume = smallest_enclosing_cylinder(points)
print(f"{min_volume:.6f}")

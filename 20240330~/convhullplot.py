import matplotlib.pyplot as plt
from random import randint
inf=float('inf')

def sim_arctan(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if dy!=0: tilt=-dx/dy if dx!=0 else 0
    else: tilt=-inf
    return tilt

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def conv_hull(arr):
    arr = sorted(arr, key=lambda x: (x[1], x[0]))
    le = len(arr)
    if le < 3:
        return arr
    st = arr[0]
    print(st)
    arr.pop(0)
    arr = [st]+sorted(arr, key=lambda x: sim_arctan(st[0],st[1],x[0],x[1]))
    
    stack=[st,arr[1]]
    for i in range(2,le):
        nxt=arr[i]
        while len(stack)>=2 and ccw(*stack[-2],*stack[-1],*nxt)<=0:
            stack.pop()
        stack.append(arr[i])

    return arr,stack

# 사용자 입력 받기
n = 10
arr = []
while len(arr)<n:
    dot=(randint(0,3),randint(0,3))
    if dot not in arr:
        arr.append(dot)

# 원래 배열에 인덱스 추가
sorted_points,polygon = conv_hull(arr)

sorted_points=[[sorted_points[i][0],sorted_points[i][1],i] for i in range(len(sorted_points))]
print(sorted_points)

print(polygon)

# 시각화
x_coords = [point[0] for point in sorted_points]
y_coords = [point[1] for point in sorted_points]
indexes = [point[2] for point in sorted_points]

plt.figure(figsize=(10, 6))
plt.scatter(x_coords, y_coords, color='blue')

for i in range(len(sorted_points)):
    plt.text(x_coords[i], y_coords[i], f"({x_coords[i]}, {y_coords[i]})\nindex: {indexes[i]}", fontsize=9, ha='right')

plt.title("Convex Hull Points with Indices")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)
plt.show()
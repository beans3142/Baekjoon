import matplotlib.pyplot as plt
import numpy as np

# 고정된 값
a1, a2 = 25, 50
b1, b2 = 100, 50
n1, n2 = a1 + b1, a2 + b2

# 기존 결과 계산
def getRes(x, y):
    res1 = y * x**2
    res2 = (n1 - x) * (n2 - y)
    flag = res1 - 500000 > 0 and res2 - 1250 > 0
    if flag:
        return ((res1 - 500000, res2 - 1250), res1, res2, x, y)
    else:
        return -1

result = []
for x in range(125):
    for y in range(100):
        res = getRes(x, y)
        if res != -1:
            result.append(res)

# 산점도 데이터
xs = [item[-2] for item in result]  # x
ys = [item[-1] for item in result]  # y

# 격자 데이터 생성
x_range = np.linspace(0, 125, 300)
y_range = np.linspace(0, 100, 300)
X, Y = np.meshgrid(x_range, y_range)

# 조건 곡선 계산
res1 = Y * X**2
res2 = (n1 - X) * (n2 - Y)

# 플롯
plt.figure(figsize=(12, 7))
plt.scatter(xs, ys, c='blue', alpha=0.6, edgecolors='w', label='Valid (x, y)')

# 조건 경계선 그리기 (res1 = 500000, res2 = 1250)
contour1 = plt.contour(X, Y, res1, levels=[500000], colors='red', linestyles='dashed')
contour2 = plt.contour(X, Y, res2, levels=[1250], colors='green', linestyles='dotted')

# 라벨 추가
contour1.collections[0].set_label('res1 = 500000 (y·x²)')
contour2.collections[0].set_label('res2 = 1250 ((n1-x)(n2-y))')

# 제목 및 축
plt.title('조건을 만족하는 (x, y) 좌표 분포와 경계선')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

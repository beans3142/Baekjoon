import sys
import bisect
si = sys.stdin.readline
 
n = int(si())
solutions = [int(e) for e in si().split()]
solutions.sort()
if solutions[0] <= 0 and solutions[-1] <= 0:
    print(solutions[-3], solutions[-2], solutions[-1])
    exit()
if solutions[0] >= 0 and solutions[-1] >= 0:
    print(solutions[0], solutions[1], solutions[2])
    exit()
mx, flag = int(3e9+1), False
for idx in range(n-2):
    target, s, e = -solutions[idx], idx+1, n-1
    while s < e:
        temp = solutions[s]+solutions[e]
        total = temp+solutions[idx]
        if abs(total) < mx:
            mx = abs(total)
            ans1, ans2, ans3 = solutions[idx], solutions[s], solutions[e]
            if not total:
                flag = True
                break
        if temp < target:
            s += 1
        else:
            e -= 1
    if flag:
        break
 
print(ans1, ans2, ans3)


from sys import stdin
from collections import Counter

def mkcase(n, vi, case, use):
    able = True
    le = len(case)
    cc = []
    for i in range(le):
        if case[i] + n in vi:
            cc.append(case[i] + n)
        else:
            able = False
            break
    if able:
        use.append(n)
        for i in cc:
            vi[i] -= 1
            if vi[i] == 0:
                del vi[i]
        case.extend(cc)

def restore_sequence(n, nums):
    nums.sort()
    vi = Counter(nums)
    use = []
    case = [0]
    
    for num in nums:
        if num not in vi:
            continue
        mkcase(num, vi, case, use)
    
    return sorted(use)

# 입력 받기
n = int(input())
nums = list(map(int, input().split()))

# 원래 수열 복원 및 출력
result = restore_sequence(n, nums)
print(" ".join(map(str, result)))

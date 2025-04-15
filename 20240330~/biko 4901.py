import bisect

n, q = map(int, input().split())
arr = sorted(map(int, input().split()))
pre = [float('inf')] * (n + 1)
suf = [float('inf')] * (n + 1)
pre[0] = 0
suf[n] = 0

# pre 계산 (왼쪽 -> 오른쪽)
for i in range(3, n + 1):
    for j in range(3, 6):
        if i - j >= 0:
            pre[i] = min(pre[i], pre[i - j] + 2 * (arr[i - 1] - arr[i - j]))

# suf 계산 (오른쪽 -> 왼쪽)
for i in range(n - 3, -1, -1):
    for j in range(3, 6):
        if i + j <= n:
            suf[i] = min(suf[i], suf[i + j] + 2 * (arr[i + j - 1] - arr[i]))

# 쿼리 처리
res = []
for _ in range(q):
    _, x = input().split()
    x = int(x)

    # 초청 선수가 들어갈 위치
    idx = bisect.bisect_left(arr, x)

    # 현재 최소 불균형 계산
    mn = float('inf')
    if idx >= 3:  # 왼쪽 pre 값을 활용
        mn = min(mn, pre[idx])
    if idx + 3 <= n:  # 오른쪽 suf 값을 활용
        mn = min(mn, suf[idx])

    # 초청 선수를 포함한 새로운 팀 계산
    for j in range(3, 6):
        # 왼쪽에 초청 선수를 포함
        if idx - j + 1 >= 0:
            mn = min(mn, pre[idx - j + 1] + 2 * (x - arr[idx - j]))
        # 오른쪽에 초청 선수를 포함
        if idx + j - 1 <= n - 1:
            mn = min(mn, suf[idx + j - 1] + 2 * (arr[idx + j - 1] - x))

    res.append(mn)

print('\n'.join(map(str, res)))

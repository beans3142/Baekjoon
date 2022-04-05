MIN=-(10**15)
n=int(input())
arr=list(map(int,input().split()))

if True:
    def find(lo, hi):
        # 1.
        if lo == hi:
            return arr[lo]

        mid = (lo + hi) // 2
	# 2.
        left = find(lo, mid)
        right = find(mid+1, hi)

        # 3.
        tmp = 0
        left_part = MIN
        for i in range(mid, lo-1, -1):
            tmp += arr[i]
            left_part = max(left_part, tmp)

        tmp = 0
        right_part = MIN
        for i in range(mid+1, hi+1):
            tmp += arr[i]
            right_part = max(right_part, tmp)

        # 4.
        return max(left, right, left_part + right_part)

print(find(0,n-1))

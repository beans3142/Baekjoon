import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
rev = arr[:]
up = down = 0

def sort(a, asc):
    global up, down
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for i in range(n - 1):
            if (asc and a[i] > a[i + 1]) or (not asc and a[i] < a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                up += asc
                down += not asc
                sorted_flag = False

sort(arr, True)
sort(rev, False)

print(min(up, down))

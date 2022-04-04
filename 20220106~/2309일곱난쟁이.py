import sys
input=sys.stdin.readline
arr=[int(input()) for i in range(9)]
total=sum(arr)

for i in range(8):
    for j in range(i+1,9):
        if total-arr[i]-arr[j]==100:
            for x in sorted(arr):
                if x!=arr[i] and x!=arr[j]:
                    print(x)
            exit()

from sys import stdin
input=stdin.readline
n=int(input())
# 2 4 6 9 12 16 20

# 2 2 3 3 4 4 5 5
arr=[i//2 for i in range(4,204)]
print(2+sum(arr[:n-1]))

import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    m=int(input())
    if m==0:
        arr.pop(-1)
    else:
        arr.append(m)

print(sum(arr))

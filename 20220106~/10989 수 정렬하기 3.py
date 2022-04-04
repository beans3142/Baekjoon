import sys
input=sys.stdin.readline

n=int(input())
'''
arr=[int(input()) for i in range(int(input()))]
for i in sorted(arr):
    print(i)
'''
arr={}
for i in range(n):
    m=int(input())
    if m not in arr:
        arr[m]=1
    else:
        arr[m]+=1

for i in sorted(arr):
    for j in range(arr[i]):
        print(i)

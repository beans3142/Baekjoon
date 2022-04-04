import sys

input=sys.stdin.readline

arr={}

for i in range(int(input())):
    w=input().rstrip()
    if len(w) not in arr:
        arr[len(w)]=[w]
    else:
        if w not in arr[len(w)]:
            arr[len(w)]+=[w]

for i in sorted(arr):
    for j in sorted(arr[i]):
        print(j)

'''
arr={input().rstrip()for i in range(int(input()))

arr=sorted(arr)
''' 
        

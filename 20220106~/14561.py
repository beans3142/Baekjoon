from sys import stdin
input=stdin.readline

def njin(n,b):
    arr=[]
    while n:
        arr.append(n%b)
        n//=b
    return arr

def is_pal(arr):
    for i in range(len(arr)):
        if arr[~i]!=arr[i]:
            return 0
    return 1

for i in range(int(input())):
    a,n=map(int,input().split())
    b=njin(a,n)
    print(is_pal(b))

from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
arr1=map(int,input().split())
arr2=map(int,input().split())

arr=[]
try:
    a=next(arr1)
    b=next(arr2)
    while True:
        if a>b:
            arr.append(b)
            b=next(arr2)
        else:
            arr.append(a)
            a=next(arr1)
except:
    try:
        if a==arr[-1]:
            while True:
                arr.append(b)
                b=next(arr2)
        if b==arr[-1]:
            while True:
                arr.append(a)
                a=next(arr1)
    except:
        print(*arr)

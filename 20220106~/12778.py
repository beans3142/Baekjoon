from sys import stdin
input=stdin.readline

t=int(input())
for i in range(t):
    n,typ=input().rstrip().split()
    arr=input().rstrip().split()
    if typ=='C':
        for i in range(int(n)):
            arr[i]=ord(arr[i])-64
    else:
        for i in range(int(n)):
            arr[i]=chr(64+int(arr[i]))
    print(*arr)
